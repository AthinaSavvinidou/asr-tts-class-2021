import glob, os
import random
import pandas as pd

root_dir = "/data/voxforge_german/audio/"

prompt_lines = []
prompts = []
audio_files = []

for filename in glob.iglob(root_dir + '**/*.wav', recursive=True):
     audio_files.append(filename)

for filename in glob.iglob(root_dir + '**/PROMPTS', recursive=True):
        with open(filename, 'r', encoding="ISO-8859-1") as file:
            # print(filename)encoding="utf8", errors='ignore'
            for line in file:
                cline = line.rstrip('\n')
                prompt_lines.append(cline)


num_audio_files = len(audio_files)

dev_split = 0.2

n_train = int(num_audio_files * (1-dev_split))
n_dev = num_audio_files - n_train

random.shuffle(audio_files)

df = pd.DataFrame(columns=["client_id", "id", "path", "sentence"])

for filepath in audio_files:
    speaker = filepath.split(os.path.sep)[4]
    filename = filepath.split(os.path.sep)[-1].split(".")[0]
    for pr in prompt_lines:
        if pr.find(speaker)>=0 and pr.find(filename)>=0:
            idx, sentence = pr.split(" ", 1)
            df = df.append({'client_id': speaker, "id": idx, "path": filepath, "sentence": sentence}, ignore_index=True)
            break

df['sentence'] = df['sentence'].str.replace(r'[^\w\s]+',' ', regex=True)

df_train = df[:n_train].copy().sort_values(by=['id'])
df_dev = df[n_train:].copy().sort_values(by=['id'])

train_folder = 'train'
if not os.path.exists(train_folder):
    os.mkdir(train_folder)
df_train.to_csv(os.path.join(train_folder, 'train.tsv'), sep='\t', index=False, header=True)
df_train[['id', 'path']].to_csv(os.path.join(train_folder, 'wav.scp'), sep=' ', index=False, header=False)
df_train[['id', 'sentence']].to_csv(os.path.join(train_folder, 'text'), sep='\t', index=False, header=False)
df_train[['id', 'client_id']].to_csv(os.path.join(train_folder, "utt2spk"), quotechar=' ', sep=' ', index=False, header=False)

dev_folder = 'dev'
if not os.path.exists(dev_folder):
    os.mkdir(dev_folder)
df_dev.to_csv(os.path.join(dev_folder, 'train.tsv'), sep='\t', index=False, header=True)
df_dev[['id', 'path']].to_csv(os.path.join(dev_folder, 'wav.scp'), sep=' ', index=False, header=False)
df_dev[['id', 'sentence']].to_csv(os.path.join(dev_folder, 'text'), sep='\t', index=False, header=False)
df_dev[['id', 'client_id']].to_csv(os.path.join(dev_folder, "utt2spk"), quotechar=' ', sep=' ', index=False, header=False)

