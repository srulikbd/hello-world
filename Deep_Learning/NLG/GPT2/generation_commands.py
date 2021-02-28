import os
import pandas as pd
sentences = ['A tweet talking about the fake elections: ']
sentences = pd.read_excel(r"/home/ubuntu/GPT2/sentences for generation/covid.xlsx", header=None)[0].tolist()
print(sentences)
cmd = 'python3 /home/ubuntu/transformers/examples/text-generation/run_generation.py \
--model_type gpt2 \
--model_name_or_path /home/ubuntu/models/english/GPT2-large_en_radical_islam_100K/ \
--temperature 0.95 \
--repetition_penalty 1 \
--num_return_sequences 3 \
--length 200 \
--prompt '

for sentence in sentences:
    returned_value = os.system(cmd + "'" + sentence.strip() + "'")
    print(returned_value)
    print('\n\n -------------------')