import streamlit as st

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.imgur.com/ptmLoCO.png");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

faq_data = [
    {
        "question": "What is lorem ipsum?",
        "answer": "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
    },
    {
        "question": "Can I see a Game of Thrones ipsum?",
        "answer": "Hodor. Hodor hodor, hodor. Hodor hodor hodor hodor hodor..."
    },
    {
        "question": "Is a Trump ipsum possible?",
        "answer": "Lorem Ipsum is the single greatest threat. We are not..."
    },
    {
        "question": "How about an academic ipsum?",
        "answer": "If one examines precultural libertarianism, one is faced with..."
    },
    {
        "question": "Is a Breaking Bad ipsum also possible?",
        "answer": "A business big enough that it could be listed on the NASDAQ goes belly up..."
    },
    {
        "question": "What does a hipster ipsum look like?",
        "answer": "Lorem ipsum dolor amet mustache knausgaard +1, blue bottle waistcoat tbh..."
    },
]

# Set the title style
st.markdown(
    """
    <h1 style='text-align: center; color: #FF5722; font-weight: bold;'>Frequently Asked Questions</h1>
    """,
    unsafe_allow_html=True
)

# Set the container style with background color
st.markdown(
    """
    <style>
    .faq-expander .content {
        color: #FFFFFF;
    }
    .faq-expander {
        background-color: #FFFFFF;
    }
    .faq-expander .st-expander {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

for faq in faq_data:
    expander = st.expander(faq["question"], expanded=False)
    with expander:
        st.markdown(
            f"""
            <div class="content">
                {faq["answer"]}
            </div>
            """,
            unsafe_allow_html=True
        )
