# # # # import streamlit as st
# # # # from streamlit_drawable_canvas import st_canvas
# # # # from PIL import Image
# # # # import google.generativeai as genai
# # # # import base64
# # # # import io

# # # # # Configure Gemini API
# # # # genai.configure(api_key="AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU ")
# # # # model = genai.GenerativeModel("gemini-2.0-flash")

# # # # # Streamlit UI
# # # # st.title("Handwritten Math Solver with Gemini AI")
# # # # st.write("Draw your math equation below and click 'Solve'.")

# # # # # Create a canvas where users can write equations
# # # # canvas_result = st_canvas(
# # # #     fill_color="rgba(255, 255, 255, 0)",
# # # #     stroke_width=5,
# # # #     stroke_color="#000000",
# # # #     background_color="#FFFFFF",
# # # #     height=200,
# # # #     width=400,
# # # #     drawing_mode="freedraw",
# # # #     key="canvas",
# # # # )

# # # # # Convert canvas drawing to image
# # # # def get_canvas_image():
# # # #     if canvas_result.image_data is not None:
# # # #         img = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
# # # #         buffered = io.BytesIO()
# # # #         img.save(buffered, format="PNG")
# # # #         return buffered.getvalue()
# # # #     return None

# # # # # Process and send to Gemini AI
# # # # if st.button("Solve"):
# # # #     image_data = get_canvas_image()
# # # #     if image_data:
# # # #         # Convert image to base64
# # # #         img_base64 = base64.b64encode(image_data).decode("utf-8")
        
# # # #         # Send request to Gemini AI
# # # #         response = model.generate_content([
# # # #             {"inline_data": {"mime_type": "image/png", "data": img_base64}},
# # # #             {"text": "Solve this handwritten math equation."}
# # # #         ])
        
# # # #         # Display the solution
# # # #         st.subheader("Solution:")
# # # #         st.write(response.text if response else "Could not recognize the equation.")
# # # #     else:
# # # #         st.warning("Please draw an equation before clicking Solve.")
# # # import streamlit as st
# # # from streamlit_drawable_canvas import st_canvas
# # # from PIL import Image
# # # import google.generativeai as genai
# # # import base64
# # # import io

# # # # Configure Gemini API
# # # genai.configure(api_key="AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU")
# # # model = genai.GenerativeModel("gemini-2.0-flash")

# # # # Streamlit UI
# # # st.title("Handwritten Math Solver with Gemini AI")
# # # st.write("Write a math equation below and click 'Solve'.")

# # # # Canvas for drawing equations
# # # canvas_result = st_canvas(
# # #     fill_color="rgba(255, 255, 255, 0)",
# # #     stroke_width=5,
# # #     stroke_color="#000000",
# # #     background_color="#FFFFFF",
# # #     height=200,
# # #     width=400,
# # #     drawing_mode="freedraw",
# # #     key="canvas",
# # # )

# # # # Convert canvas drawing to image
# # # def get_canvas_image():
# # #     if canvas_result.image_data is not None:
# # #         img = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
# # #         buffered = io.BytesIO()
# # #         img.save(buffered, format="PNG")
# # #         return buffered.getvalue()
# # #     return None

# # # # When user clicks "Solve"
# # # if st.button("Solve"):
# # #     image_data = get_canvas_image()
# # #     if image_data:
# # #         # Convert image to Base64
# # #         img_base64 = base64.b64encode(image_data).decode("utf-8")

# # #         # Send the image to Gemini AI
# # #         response = model.generate_content([
# # #             {"inline_data": {"mime_type": "image/png", "data": img_base64}},
# # #             {"text": "Solve the handwritten math equation in this image."}
# # #         ])

# # #         # Display solution
# # #         st.subheader("Solution:")
# # #         st.write(response.text if response else "Could not interpret the equation.")
# # #     else:
# # #         st.warning("Please draw an equation before clicking Solve.")
# # import streamlit as st
# # from streamlit_drawable_canvas import st_canvas
# # from PIL import Image
# # import google.generativeai as genai
# # import speech_recognition as sr
# # from gtts import gTTS
# # import base64
# # import io
# # import os

# # # Configure Google Gemini API
# # genai.configure(api_key="AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU")
# # model = genai.GenerativeModel("gemini-2.0-flash")

# # # **Function: Convert text to speech (TTS)**
# # def text_to_speech(text, filename="solution.mp3"):
# #     tts = gTTS(text=text, lang="en")
# #     tts.save(filename)
# #     return filename

# # # **Function: Convert speech to text (STT)**
# # def speech_to_text():
# #     recognizer = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         st.write("🎤 Listening... Speak now!")
# #         audio = recognizer.listen(source)
# #         try:
# #             return recognizer.recognize_google(audio)
# #         except sr.UnknownValueError:
# #             return "Could not understand audio."
# #         except sr.RequestError:
# #             return "Speech recognition service is unavailable."

# # # **Function: Encode image to Base64**
# # def encode_image(image_data):
# #     return base64.b64encode(image_data).decode("utf-8")

# # # **Function: Get image from canvas**
# # def get_canvas_image():
# #     if canvas_result.image_data is not None:
# #         img = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
# #         buffered = io.BytesIO()
# #         img.save(buffered, format="PNG")
# #         return buffered.getvalue()
# #     return None

# # # **Streamlit UI**
# # st.title("📝 Handwritten Math Solver & AI Search")
# # st.write("Write a math equation, upload an image, or speak a query.")

# # # **Brush & Eraser settings**
# # col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
# # with col1:
# #     stroke_color = st.color_picker("🎨 Brush Color", "#000000")
# # with col2:
# #     stroke_width = st.slider("✏️ Brush Size", 1, 20, 5)
# # with col3:
# #     eraser_width = st.slider("🧽 Eraser Size", 1, 50, 20)
# # with col4:
# #     drawing_mode = st.radio("✍️ Mode", ["freedraw", "erase"], horizontal=True)

# # # **Canvas for handwritten math equations**
# # canvas_result = st_canvas(
# #     fill_color="rgba(255, 255, 255, 0)",  # Transparent background
# #     stroke_width=eraser_width if drawing_mode == "erase" else stroke_width,
# #     stroke_color="#FFFFFF" if drawing_mode == "erase" else stroke_color,  # White for eraser
# #     background_color="#FFFFFF",
# #     height=500,
# #     width=900,
# #     drawing_mode="freedraw",
# #     key="canvas",
# # )

# # # **Image upload for AI analysis**
# # uploaded_image = st.file_uploader("📤 Upload an image (Optional)", type=["png", "jpg", "jpeg"])

# # # **Speech-to-Text Button**
# # st.subheader("🎙 Speak Your Query")
# # if st.button("🎤 Start Listening"):
# #     spoken_text = speech_to_text()
# #     st.write("📝 You said:", spoken_text)

# # # **Optional text prompt for AI**
# # user_prompt = st.text_input("🔍 Enter a query", spoken_text if "spoken_text" in locals() else "")

# # # **Processing Handwritten Math**
# # image_data = get_canvas_image()
# # if image_data:
# #     img_base64 = encode_image(image_data)

# #     col1, col2 = st.columns(2)

# #     with col1:
# #         if st.button("🔢 Solve Equation"):
# #             response = model.generate_content([
# #                 {"inline_data": {"mime_type": "image/png", "data": img_base64}},
# #                 {"text": "Solve the handwritten math equation in this image and provide only the final answer."}
# #             ])
# #             st.subheader("Solution:")
# #             st.write(response.text if response else "Could not interpret the equation.")

# #             # **Convert solution to speech**
# #             if response.text:
# #                 speech_file = text_to_speech(response.text)
# #                 with open(speech_file, "rb") as f:
# #                     st.audio(f.read(), format="audio/mp3")

# #     with col2:
# #         if st.button("📖 Detailed Solution"):
# #             response = model.generate_content([
# #                 {"inline_data": {"mime_type": "image/png", "data": img_base64}},
# #                 {"text": "Solve the handwritten math equation in this image and provide a detailed step-by-step solution."}
# #             ])
# #             st.subheader("Detailed Solution:")
# #             st.write(response.text if response else "Could not interpret the equation.")

# #             # **Convert detailed solution to speech**
# #             if response.text:
# #                 speech_file = text_to_speech(response.text)
# #                 with open(speech_file, "rb") as f:
# #                     st.audio(f.read(), format="audio/mp3")

# # # **Processing Image Upload**
# # if uploaded_image:
# #     img_bytes = uploaded_image.read()
# #     img_base64 = encode_image(img_bytes)

# #     if st.button("🖼️ Analyze Image"):
# #         response = model.generate_content([
# #             {"inline_data": {"mime_type": "image/jpeg", "data": img_base64}},
# #             {"text": "Analyze this image and describe its contents in detail."}
# #         ])
# #         st.subheader("Image Analysis:")
# #         st.write(response.text if response else "Could not analyze the image.")

# #         # **Convert response to speech**
# #         if response.text:
# #             speech_file = text_to_speech(response.text)
# #             with open(speech_file, "rb") as f:
# #                 st.audio(f.read(), format="audio/mp3")

# # # **Processing Custom Query**
# # if user_prompt:
# #     if st.button("🔎 Search AI Query"):
# #         response = model.generate_content(user_prompt)
# #         st.subheader("AI Response:")
# #         st.write(response.text if response else "No response generated.")

# #         # **Convert response to speech**
# #         if response.text:
# #             speech_file = text_to_speech(response.text)
# #             with open(speech_file, "rb") as f:
# #                 st.audio(f.read(), format="audio/mp3")
# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
# from PIL import Image
# import google.generativeai as genai
# import speech_recognition as sr
# from gtts import gTTS
# import base64
# import io
# import os

# # Configure Google Gemini API
# genai.configure(api_key="AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU")
# model = genai.GenerativeModel("gemini-2.0-flash")

# # **Function: Convert text to speech (TTS)**
# def text_to_speech(text, filename="response.mp3"):
#     tts = gTTS(text=text, lang="en")
#     tts.save(filename)
#     return filename

# # **Function: Convert speech to text (STT)**
# def speech_to_text():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("🎤 Listening... Speak now!")
#         audio = recognizer.listen(source)
#         try:
#             return recognizer.recognize_google(audio)
#         except sr.UnknownValueError:
#             return "Could not understand audio."
#         except sr.RequestError:
#             return "Speech recognition service unavailable."

# # **Function: Encode image to Base64**
# def encode_image(image_data):
#     return base64.b64encode(image_data).decode("utf-8")

# # **Function: Get image from canvas**
# def get_canvas_image():
#     if canvas_result.image_data is not None:
#         img = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
#         buffered = io.BytesIO()
#         img.save(buffered, format="PNG")
#         return buffered.getvalue()
#     return None

# # **Streamlit UI**
# st.title("📝 Handwritten Math Solver & AI Search")
# st.write("Write a math equation, upload an image, or speak a query.")

# # **Brush & Eraser settings**
# col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
# with col1:
#     stroke_color = st.color_picker("🎨 Brush Color", "#000000")
# with col2:
#     stroke_width = st.slider("✏️ Brush Size", 1, 20, 5)
# with col3:
#     eraser_width = st.slider("🧽 Eraser Size", 1, 50, 20)
# with col4:
#     drawing_mode = st.radio("✍️ Mode", ["freedraw", "erase"], horizontal=True)

# # **Canvas for handwritten math equations**
# canvas_result = st_canvas(
#     fill_color="rgba(255, 255, 255, 0)",
#     stroke_width=eraser_width if drawing_mode == "erase" else stroke_width,
#     stroke_color="#FFFFFF" if drawing_mode == "erase" else stroke_color,
#     background_color="#FFFFFF",
#     height=500,
#     width=900,
#     drawing_mode="freedraw",
#     key="canvas",
# )

# # **Image upload for AI analysis**
# uploaded_image = st.file_uploader("📤 Upload an image (Optional)", type=["png", "jpg", "jpeg"])

# # **Speech-to-Text Button**
# st.subheader("🎙 Speak Your Query")
# if st.button("🎤 Start Listening"):
#     spoken_text = speech_to_text()
#     st.write("📝 You said:", spoken_text)

# # **Optional text prompt for AI**
# user_prompt = st.text_input("🔍 Enter a query", spoken_text if "spoken_text" in locals() else "")

# # **Processing Handwritten Math**
# image_data = get_canvas_image()
# if image_data:
#     img_base64 = encode_image(image_data)

#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("🔢 Solve Equation"):
#             response = model.generate_content([
#                 {"inline_data": {"mime_type": "image/png", "data": img_base64}},
#                 {"text": "Solve the handwritten math equation in this image and provide only the final answer."}
#             ])
#             st.subheader("Solution:")
#             st.write(response.text if response else "Could not interpret the equation.")

#             # **Convert solution to speech**
#             if response.text:
#                 speech_file = text_to_speech(response.text)
#                 with open(speech_file, "rb") as f:
#                     st.audio(f.read(), format="audio/mp3")

#     with col2:
#         if st.button("📖 Detailed Solution"):
#             response = model.generate_content([
#                 {"inline_data": {"mime_type": "image/png", "data": img_base64}},
#                 {"text": "Solve the handwritten math equation in this image and provide a detailed step-by-step solution."}
#             ])
#             st.subheader("Detailed Solution:")
#             st.write(response.text if response else "Could not interpret the equation.")

#             # **Convert detailed solution to speech**
#             if response.text:
#                 speech_file = text_to_speech(response.text)
#                 with open(speech_file, "rb") as f:
#                     st.audio(f.read(), format="audio/mp3")

# # **Processing Image Upload**
# if uploaded_image:
#     img_bytes = uploaded_image.read()
#     img_base64 = encode_image(img_bytes)

#     if st.button("🖼️ Analyze Image"):
#         response = model.generate_content([
#             {"inline_data": {"mime_type": "image/jpeg", "data": img_base64}},
#             {"text": "Analyze this image and describe its contents in detail."}
#         ])
#         st.subheader("Image Analysis:")
#         st.write(response.text if response else "Could not analyze the image.")

#         # **Convert response to speech**
#         if response.text:
#             speech_file = text_to_speech(response.text)
#             with open(speech_file, "rb") as f:
#                 st.audio(f.read(), format="audio/mp3")

# # **Processing Custom Query**
# if user_prompt:
#     if st.button("🔎 Search AI Query"):
#         response = model.generate_content(user_prompt)
#         st.subheader("AI Response:")
#         st.write(response.text if response else "No response generated.")

#         # **Convert AI response to speech**
#         if response.text:
#             speech_file = text_to_speech(response.text)
#             with open(speech_file, "rb") as f:
#                 st.audio(f.read(), format="audio/mp3")
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import base64
import io
import os

# Configure Google Gemini API (use environment variable for deployment)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY", "AIzaSyAWsewWyrj733ImgncO47SwlsKmm-5pDKU"))
model = genai.GenerativeModel("gemini-2.0-flash")  # Update to correct model if needed

# Custom CSS for Sky-Blue Theme
st.markdown("""
    <style>
    body {
        background-color: #e0f2fe;
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background-color: #e0f2fe;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1, h2, h3 {
        color: #0369a1;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #0284c7;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #0369a1;
    }
    .stTextInput>input, .stTextArea>textarea {
        border: 2px solid #7dd3fc;
        border-radius: 8px;
        background-color: #f0f9ff;
        color: #0c4a6e;
    }
    .stRadio>label, .stColorPicker, .stSlider {
        background-color: #f0f9ff;
        border: 2px solid #7dd3fc;
        border-radius: 8px;
        padding: 5px;
    }
    .stFileUploader {
        background-color: #f0f9ff;
        border: 2px dashed #7dd3fc;
        border-radius: 8px;
        padding: 10px;
    }
    .stSuccess, .stWarning, .stError {
        background-color: #bae6fd;
        border: 1px solid #7dd3fc;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# **Function: Convert text to speech (TTS)**
def text_to_speech(text, filename="response.mp3"):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        return filename
    except Exception as e:
        st.error(f"🚫 TTS Error: {str(e)}")
        return None

# **Function: Convert speech to text (STT)**
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening... Speak now!")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio."
        except sr.RequestError:
            return "Speech recognition service unavailable."

# **Function: Encode image to Base64**
def encode_image(image_data):
    return base64.b64encode(image_data).decode("utf-8")

# **Function: Get image from canvas**
def get_canvas_image():
    if canvas_result.image_data is not None:
        img = Image.fromarray((canvas_result.image_data * 255).astype("uint8"))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return buffered.getvalue()
    return None

# **Streamlit UI**
st.title("📝 Handwritten Math Solver & AI Search")
st.write("✨ Write a math equation, upload an image (up to 1 GB), or speak a query!")

# **Brush & Eraser settings**
st.subheader("🛠️ Drawing Settings")
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    stroke_color = st.color_picker("🎨 Brush Color", "#0284c7")  # Sky-blue default
with col2:
    stroke_width = st.slider("✏️ Brush Size", 1, 20, 5)
with col3:
    eraser_width = st.slider("🧽 Eraser Size", 1, 50, 20)
with col4:
    drawing_mode = st.radio("✍️ Mode", ["freedraw", "erase"], horizontal=True)

# **Canvas for handwritten math equations**
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0)",
    stroke_width=eraser_width if drawing_mode == "erase" else stroke_width,
    stroke_color="#FFFFFF" if drawing_mode == "erase" else stroke_color,
    background_color="#FFFFFF",
    height=600,  # Increased from 500 to 600
    width=900,
    drawing_mode="freedraw" if drawing_mode == "freedraw" else "freedraw",  # Always freedraw, toggled by erase mode
    key="canvas",
)

# **Image upload for AI analysis**
st.subheader("📤 Upload an Image")
uploaded_image = st.file_uploader(
    "Drag and drop file here - Limit 1 GB per file • PNG, JPG, JPEG",
    type=["png", "jpg", "jpeg"]
)

# **Speech-to-Text Button**
st.subheader("🎙 Speak Your Query")
if st.button("🎤 Start Listening"):
    spoken_text = speech_to_text()
    st.write("📝 You said:", spoken_text)

# **Optional text prompt for AI**
user_prompt = st.text_input("🔍 Enter a query", spoken_text if "spoken_text" in locals() else "", 
                            placeholder="e.g., Solve 2x + 3 = 7")

# **Processing Handwritten Math**
image_data = get_canvas_image()
if image_data:
    img_base64 = encode_image(image_data)

    st.subheader("🔢 Math Equation Options")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔢 Solve Equation"):
            response = model.generate_content([
                {"inline_data": {"mime_type": "image/png", "data": img_base64}},
                {"text": "Solve the handwritten math equation in this image and provide only the final answer."}
            ])
            st.subheader("🌟 Solution:")
            st.write(response.text if response else "Could not interpret the equation.")

            # **Convert solution to speech**
            if response and response.text:
                speech_file = text_to_speech(response.text)
                if speech_file:
                    with open(speech_file, "rb") as f:
                        st.audio(f.read(), format="audio/mp3")
                    os.remove(speech_file)

    with col2:
        if st.button("📖 Detailed Solution"):
            response = model.generate_content([
                {"inline_data": {"mime_type": "image/png", "data": img_base64}},
                {"text": "Solve the handwritten math equation in this image and provide a detailed step-by-step solution."}
            ])
            st.subheader("🌟 Detailed Solution:")
            st.write(response.text if response else "Could not interpret the equation.")

            # **Convert detailed solution to speech**
            if response and response.text:
                speech_file = text_to_speech(response.text)
                if speech_file:
                    with open(speech_file, "rb") as f:
                        st.audio(f.read(), format="audio/mp3")
                    os.remove(speech_file)

# **Processing Image Upload**
if uploaded_image:
    img_bytes = uploaded_image.read()
    img_base64 = encode_image(img_bytes)

    if st.button("🖼️ Analyze Image"):
        response = model.generate_content([
            {"inline_data": {"mime_type": "image/jpeg", "data": img_base64}},
            {"text": "Analyze this image and describe its contents in detail."}
        ])
        st.subheader("🌟 Image Analysis:")
        st.write(response.text if response else "Could not analyze the image.")

        # **Convert response to speech**
        if response and response.text:
            speech_file = text_to_speech(response.text)
            if speech_file:
                with open(speech_file, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                os.remove(speech_file)

# **Processing Custom Query**
if user_prompt:
    if st.button("🔎 Search AI Query"):
        response = model.generate_content(user_prompt)
        st.subheader("🌟 AI Response:")
        st.write(response.text if response else "No response generated.")

        # **Convert AI response to speech**
        if response and response.text:
            speech_file = text_to_speech(response.text)
            if speech_file:
                with open(speech_file, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                os.remove(speech_file)

st.success("✅ Ready! Draw, upload (up to 1 GB), or speak your query!")