import google.generativeai as genai
import streamlit as st

model = genai.GenerativeModel('gemini-pro')
genai.configure(api_key="API Key")

def detect_spam(input_text, category, explanation, model):
    # check if a category is specified, otherwise default to spam, not_spam, unknown
    category = category if category else 'spam, not_spam, unknown'
    # check if explanation is required
    explanation_text = 'provide short explanation' if explanation else 'no explanation'
    # question to be asked
    question = f'''Given the input text, perform spam detection on it
    {category}
    {input_text}
    {explanation_text}
    '''
    # generate response
    response = model.generate_content(question)
    return response.text.strip()
# user_input = "you have just won $14000, claim this award here at this link."
# category = 'spam, not_spam, unknown'

# spam_result = detect_spam(input_text=user_input, category=category, explanation=True, model=model)

# print(spam_result)

def main():
    st.title("Spam classification")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Spam classification ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    user_input = st.text_input("Message:","Type Here")
    category = 'spam, not_spam, unknown'
    if st.button("Predict"):
        spam_result = detect_spam(input_text=user_input, category=category, explanation=True, model=model)
        st.success('The output is {}'.format(spam_result))

if __name__=='__main__':
    main()
