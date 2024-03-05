# source $HOME/.zshrc 2>~/error_log.txt
# conda activate wa


export OPENAI_API_KEY=YOUR_KEY

function eval {
    MODEL_NAME=${1}
    cd /home/jcx/Desktop/translation/jaen_alignment/chatgpt_word_alignment/LLM_embeddings/FastChat/fastchat/llm_judge/data/mt_bench/model_answer

    python build_answer.py $MODEL_NAME

    cd /home/jcx/Desktop/translation/jaen_alignment/chatgpt_word_alignment/LLM_embeddings/FastChat/fastchat/llm_judge/
    python gen_judgment.py --model-list $MODEL_NAME --parallel 16

    # python show_result.py --model-list $MODEL_NAME
}


eval st_openwebtext-lora-100k-distilled-gpt35-ar-3_epoch-merged-chat-fp32-QA_template
python show_result.py 
