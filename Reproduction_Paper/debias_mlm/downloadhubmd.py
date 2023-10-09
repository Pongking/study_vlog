from huggingface_hub import snapshot_download
import os

current_path=os.getcwd()
local_dir=current_path+"/my_model/"
# repo_name="dslim/bert-large-NER"
repo_name="bert-base-uncased"
snapshot_download(repo_id=repo_name,allow_patterns=["*.json","pytorch_model.bin","vocab.txt"],local_dir=local_dir+repo_name)
