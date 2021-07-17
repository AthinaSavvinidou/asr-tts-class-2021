#!/usr/bin/env bash

# Create tsv file and all required files (wav.scp, utt2spk, text) for train and dev
python3 local/prep_tsv.py

for dst in train dev; do

  wav_scp=$dst/wav.scp
  trans=$dst/text
  utt2spk=$dst/utt2spk

  spk2utt=$dst/spk2utt
  /opt/kaldi/egs/voxforge_german/s5/utils/utt2spk_to_spk2utt.pl <$utt2spk >$spk2utt || exit 1

  #Data validation
  ntrans=$(wc -l <$trans)
  nutt2spk=$(wc -l <$utt2spk)
  ! [ "$ntrans" -eq "$nutt2spk" ] && \
    echo "Inconsistent #transcripts($ntrans) and #utt2spk($nutt2spk)" && exit 1;

  /opt/kaldi/egs/voxforge_german/s5/utils/validate_data_dir.sh --no-feats $dst || exit 1;

  echo "$0: successfully prepared data in $dst"
done
exit 0