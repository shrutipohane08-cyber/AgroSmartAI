
import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AgroSmart AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("crop_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error("Model file not found. Please keep crop_model.pkl in the same folder as app.py.")
    st.stop()


# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "users" not in st.session_state:
    st.session_state.users = {"farmer": "farm123"}

if "username" not in st.session_state:
    st.session_state.username = ""


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background-color: #F8F6EF;
    color: #263C2A;
}

header[data-testid="stHeader"] {
    background-color: #F8F6EF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #23452E !important;
}

/* Normal text */
p, label, .stMarkdown, span {
    color: #344638;
}

/* Input boxes */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #263C2A !important;
    border-radius: 8px !important;
}

/* Input labels */
.stTextInput label,
.stNumberInput label,
.stSelectbox label {
    color: #23452E !important;
    font-weight: 600 !important;
}

/* ALL BUTTONS */
.stButton button,
.stFormSubmitButton button {
    background-color: #31583A !important;
    color: #FFFFFF !important;
    border: 1px solid #31583A !important;
    border-radius: 9px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
    transition: 0.2s ease-in-out;
}

/* Force button text to white */
.stButton button p,
.stFormSubmitButton button p,
.stButton button span,
.stFormSubmitButton button span {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

/* Button hover */
.stButton button:hover,
.stFormSubmitButton button:hover {
    background-color: #23452E !important;
    color: #FFFFFF !important;
    border-color: #23452E !important;
    transform: translateY(-1px);
}

/* Keep text white on hover */
.stButton button:hover p,
.stFormSubmitButton button:hover p,
.stButton button:hover span,
.stFormSubmitButton button:hover span {
    color: #FFFFFF !important;
}

/* Radio buttons */
.stRadio label {
    color: #23452E !important;
}

/* Divider */
hr {
    border-color: #D9E1D4;
}

/* Information boxes */
div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Feature cards */
.feature-card {
    background-color: #FFFFFF;
    border: 1px solid #E1E6DB;
    border-radius: 14px;
    padding: 22px;
    min-height: 150px;
    margin-bottom: 15px;
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 8px;
}

.feature-title {
    color: #23452E;
    font-weight: 700;
    font-size: 18px;
}

.feature-description {
    color: #68766A;
    font-size: 14px;
    line-height: 1.6;
}

.hero-box {
    background: linear-gradient(135deg, #E8EFE1, #F8F6EF);
    border: 1px solid #DCE5D5;
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 25px;
}

.small-note {
    font-size: 12px;
    color: #718071;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
def show_header():
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(
            "<h2 style='margin-bottom:0;'>🌱 AgroSmart AI</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='color:#68766A;margin-top:0;'>Smart farming starts with better decisions.</p>",
            unsafe_allow_html=True
        )

    with col2:
        if st.session_state.logged_in:
            st.markdown(
                f"<p style='text-align:right;padding-top:10px;'>👨‍🌾 "
                f"{st.session_state.username}</p>",
                unsafe_allow_html=True
            )

    st.divider()


# ---------------- LOGIN PAGE ----------------
def login_page():
    show_header()

    left, right = st.columns([1.1, 1], gap="large")

    with left:
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <h1 style='font-size:48px;line-height:1.2;'>
            Grow smarter.<br>
            Harvest better.
            </h1>
            <p style='font-size:17px;color:#68766A;line-height:1.8;'>
            Make informed crop choices with AgroSmart AI.
            Enter your soil and weather conditions to explore
            a machine-learning-based crop recommendation.
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🌾</div>
                <div class="feature-title">Crop Recommendation</div>
                <div class="feature-description">
                Explore a crop prediction based on soil nutrients,
                temperature, humidity, pH and rainfall.
                </div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌿</div>
                <div class="feature-title">Designed for Farmers</div>
                <div class="feature-description">
                A simple and friendly experience for exploring
                agriculture data with AI.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            "<p class='small-note'>Educational machine-learning project.</p>",
            unsafe_allow_html=True
        )

    with right:
        st.markdown("<br>", unsafe_allow_html=True)

        st.image(
            "https://images.unsplash.com/photo-1500382017468-9049fed747ef"
            "?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        login_tab, signup_tab = st.tabs(["🔐 Login", "✨ Create Account"])

        with login_tab:
            st.subheader("Welcome back!")
            st.write("Log in to continue to AgroSmart AI.")

            with st.form("login_form"):
                username = st.text_input("Username", key="login_username")
                password = st.text_input(
                    "Password",
                    type="password",
                    key="login_password"
                )
                submitted = st.form_submit_button(
                    "Login",
                    use_container_width=True
                )

            if submitted:
                if (
                    username in st.session_state.users
                    and st.session_state.users[username] == password
                ):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password. Please try again.")

            st.info("Demo login: Username: farmer | Password: farm123")

        with signup_tab:
            st.subheader("Create your account")
            st.write("Join AgroSmart AI to explore crop recommendations.")

            with st.form("signup_form"):
                new_username = st.text_input(
                    "Choose a username",
                    key="signup_username"
                )
                new_password = st.text_input(
                    "Create a password",
                    type="password",
                    key="signup_password"
                )
                confirm_password = st.text_input(
                    "Confirm password",
                    type="password",
                    key="signup_confirm_password"
                )

                signup_submitted = st.form_submit_button(
                    "Create Account",
                    use_container_width=True
                )

            if signup_submitted:
                if not new_username.strip() or not new_password:
                    st.error("Please fill in all fields.")

                elif new_username in st.session_state.users:
                    st.error("This username already exists.")

                elif len(new_password) < 6:
                    st.error("Password must contain at least 6 characters.")

                elif new_password != confirm_password:
                    st.error("Passwords do not match.")

                else:
                    st.session_state.users[new_username] = new_password
                    st.success("Account created! Please log in.")
                    st.info(
                        "Your demo account is stored only in the current session."
                    )


# ---------------- MAIN HOME PAGE ----------------
def home_page():
    show_header()

    st.markdown(
        """
        <div class="hero-box">
            <h1 style="font-size:38px;margin-bottom:8px;">
            Your farm, your future. 🌱
            </h1>
            <p style="font-size:16px;color:#68766A;line-height:1.7;">
            Welcome to your crop recommendation experience.
            Enter your field conditions below and let AgroSmart AI
            generate a crop prediction using its trained model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🌿 Crop Recommendation")
    st.write("Enter the soil and weather details for your field.")

    with st.form("crop_prediction_form"):

        st.markdown("### 🧪 Soil Nutrients")

        col1, col2, col3 = st.columns(3)

        with col1:
            nitrogen = st.number_input(
                "Nitrogen (N)",
                min_value=0.0,
                max_value=200.0,
                value=50.0,
                step=1.0
            )

        with col2:
            phosphorus = st.number_input(
                "Phosphorus (P)",
                min_value=0.0,
                max_value=200.0,
                value=50.0,
                step=1.0
            )

        with col3:
            potassium = st.number_input(
                "Potassium (K)",
                min_value=0.0,
                max_value=250.0,
                value=50.0,
                step=1.0
            )

        st.markdown("### 🌤️ Weather Conditions")

        col4, col5 = st.columns(2)

        with col4:
            temperature = st.number_input(
                "Temperature (°C)",
                min_value=-10.0,
                max_value=60.0,
                value=25.0,
                step=0.5
            )

            humidity = st.number_input(
                "Humidity (%)",
                min_value=0.0,
                max_value=100.0,
                value=70.0,
                step=1.0
            )

        with col5:
            soil_ph = st.number_input(
                "Soil pH",
                min_value=0.0,
                max_value=14.0,
                value=6.5,
                step=0.1
            )

            rainfall = st.number_input(
                "Rainfall (mm)",
                min_value=0.0,
                max_value=1000.0,
                value=100.0,
                step=5.0
            )

        submitted = st.form_submit_button(
            "🌾 Recommend a Crop",
            use_container_width=True
        )

    if submitted:
        input_data = pd.DataFrame(
            [[
                nitrogen,
                phosphorus,
                potassium,
                temperature,
                humidity,
                soil_ph,
                rainfall
            ]],
            columns=[
                "Nitrogen",
                "Phosphorus",
                "Potassium",
                "Temperature_C",
                "Humidity_pct",
                "Soil_pH",
                "Rainfall_mm"
            ]
        )

        try:
            prediction = model.predict(input_data)[0]

            st.markdown("---")
            st.markdown("## 🌱 Your Crop Prediction")

            st.success(
                f"Based on the entered values, the model predicts: **{prediction.title()}**"
            )

            st.markdown(
                """
                <div class="feature-card">
                    <div class="feature-icon">🌾</div>
                    <div class="feature-title">What does this mean?</div>
                    <div class="feature-description">
                    The model has selected this crop based on patterns
                    learned from its training dataset. This is an
                    educational prediction, not a guarantee of crop success.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.warning(
                "Important: This project uses a synthetic educational dataset. "
                "Do not use its prediction alone to make real farming decisions. "
                "Check local soil reports, climate conditions and advice from "
                "a qualified agricultural expert."
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")

    st.divider()

    st.markdown(
        """
        <p style='text-align:center;color:#718071;font-size:13px;'>
        🌱 AgroSmart AI | Smart Farming Demonstration Project
        </p>
        """,
        unsafe_allow_html=True
    )

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()


# ---------------- APP CONTROL ----------------
if st.session_state.logged_in:
    home_page()
else:
    login_page()

