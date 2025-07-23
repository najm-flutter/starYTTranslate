
# starYTTranslate

![App Screenshot](https://github.com/najm-flutter/starYTTranslate/blob/main/screenshots/Screenshot.png?raw=true)


## 📝 Project Description

`starYTTranslate` is an open-source Python project designed to simplify the process of translating YouTube video subtitles. It utilizes the Gemini AI model to accurately translate text and saves it in `.srt` format for use with video players or editing software.

## 🚀 Key Features

- 🎯 **Subtitle Extraction:** Automatically fetch subtitles from YouTube videos.
- 🌐 **Translation via Gemini AI:** Get high-quality, professional translations.
- 💾 **Save as SRT:** Compatible with most playback and editing software.
- 🖥️ **Command-Line Interface (CLI):** Simple and efficient to use.

## 🧩 Project Structure

```

starYTTranslate/
├── main.py               # Application entry point
├── menu.py               # Manages the main user menu
├── handlers/             # Service handler modules
│   ├── add_api_key.py    # Add Gemini API key
│   └── sub_translate.py  # Full translation logic
├── services/
│   ├── gemini_translate.py  # Interacts with Gemini API
│   └── sub_extract.py       # Extracts subtitles from YouTube
├── utils/
│   ├── ai_modle.py       # API key validation
│   ├── messages.py       # Error and info 
│   ├── srt_tools.py      # Tools for splitting and enhancing SRT files
│   └── welcome.py        # Welcome message for the user
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

````

## ⚙️ Requirements

- Python 3.8 or higher
- Google Gemini API key (available from [Google AI Studio](https://aistudio.google.com/))

## 💻 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/najm-flutter/starYTTranslate
cd starYTTranslate
````

### 2. Create a Virtual Environment (Optional but Recommended)

#### Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python main.py
```

You will be provided with a simple menu where you can:

* Add your Gemini API key
* Enter a YouTube video link for translation

## 🧪 How to Use

1. Run the application.
2. Add your Gemini API key when prompted or choose option 2 from the menu.
3. Choose option 1 to translate a video.
4. Enter the YouTube video URL — subtitles will be extracted, translated, and saved as an `.srt` file.

## 🤝 Contributing

We welcome contributions!

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your branch.
5. Open a Pull Request.

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---
## Feedback

If you have any feedback, please reach out to us at nagm113nagm@gmail.com

