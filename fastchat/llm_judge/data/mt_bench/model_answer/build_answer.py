
import json
import sys

model_name = sys.argv[1]

answer1 = open(f'/home/jcx/Desktop/translation/jaen_alignment/chatgpt_word_alignment/LLM_embeddings/LLaMA-Efficient-Tuning/mt_bench_result/{model_name}').readlines()
answer2 = open(f'/home/jcx/Desktop/translation/jaen_alignment/chatgpt_word_alignment/LLM_embeddings/LLaMA-Efficient-Tuning/mt_bench_result-followup/{model_name}').readlines()

data = []
for i in range(80):
    data.append({
        "question_id": 81+i, 
        "answer_id": f"{i}", 
        "model_id": model_name, 
        "choices": [{"index": 0, "turns": [answer1[i].strip(), answer2[i].strip()]}], 
        "tstamp": 1686286924.844282
    })
    
    
with open(f'{model_name}.jsonl', 'w') as file:
    for record in data:
        json_record = json.dumps(record)
        file.write(json_record + '\n')
    
