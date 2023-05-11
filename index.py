from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
model = AutoModelForCausalLM.from_pretrained("nomic-ai/gpt4all-j", revision="v1.2-jazzy", device_map='auto') 


# for token in model.generate("Tell me a joke ?"):
#     print(token, end='', flush=True)

# get response from model
def get_response(input_text):
    tokenizer = AutoTokenizer.from_pretrained("nomic-ai/gpt4all-j", revision="v1.2-jazzy")



    input_ids = tokenizer.encode(tokenizer.eos_token + input_text + ' \n', return_tensors='pt')
    response_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response_text






if __name__ == "__main__":
    # make the code recursive to get response from model
    while True:
        user_input = input(">>> ")
        if user_input == "bye" or user_input == "exit":
            break
        res = get_response(user_input)
        print(res)