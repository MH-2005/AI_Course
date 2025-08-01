# 🖼️ PixelForge - Django Image Editor

**PixelForge** is a powerful and intuitive web-based image editing application built with Python, Django, and OpenCV. It
provides a seamless experience for users to upload images, apply a variety of real-time effects, and download their
creations.

![PixelForge Screenshot](https://placehold.co/800x450/2d3748/ffffff?text=PixelForge%20UI%20Screenshot)
*A clean and responsive user interface for effortless editing.*

---

### ✨ Core Features

- **Seamless Image Upload**: Drag & drop or select common image formats like JPG, PNG, and WEBP.
- **Dual-Panel Live Preview**: Instantly compare the original image with the edited version side-by-side.
- **Image Adjustments**:
    - 🎚️ **Contrast**: Fine-tune the tonal range.
    - ☀️ **Brightness**: Lighten or darken your image with precision.
- **Creative Drawing Tools**:
    - 📏 **Draw Line**: Add straight lines with custom coordinates, color, and thickness.
    - ⬜ **Draw Rectangle**: Frame parts of your image or create geometric shapes.
- **Combined Effects**: Apply multiple transformations (e.g., adjust contrast and draw a rectangle) in a single step.
- **One-Click Download**: Save the final processed image directly to your device.

---

### 🛠️ Technology Stack

| Technology      | Description                                            |
|-----------------|--------------------------------------------------------|
| **Python**      | The core backend programming language.                 |
| **Django**      | A high-level web framework for the backend.            |
| **OpenCV**      | The primary library for image processing.              |
| **Pillow**      | A crucial library for image file handling in Django.   |
| **NumPy**       | Used for efficient numerical operations on image data. |
| **HTML5/CSS3**  | For structuring and styling the frontend.              |
| **Bootstrap 5** | A CSS framework for a responsive and modern UI.        |
| **JavaScript**  | For dynamic and interactive frontend logic.            |

---

### 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

#### Prerequisites

- Python 3.8+
- `pip` package manager
- A `git` client

#### Installation

1.**Create and activate a virtual environment:**
This isolates the project's dependencies from your system's global packages.

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

2.**Install the required packages:**
```bash
pip install -r requirements.txt
```

*(Note: If a `requirements.txt` file is not present, you can create one with `pip freeze > requirements.txt` after
installing the packages below manually.)*

```bash
pip install Django opencv-python-headless numpy Pillow
```

3.**Apply database migrations:**
This sets up the necessary database schema required by Django.

```bash
python manage.py migrate
```

4.**Run the development server:**

```bash
python manage.py runserver
```

The application will now be running and accessible at **`http://127.0.0.1:8000/`**.

---

### 📖 How to Use

1. Open your web browser and navigate to the application's URL.
2. Upload an image using the file input. The page will automatically refresh to display your image.
3. To apply an effect, **first enable its section** by clicking the corresponding checkbox (e.g., "Adjust Contrast &
   Brightness").
4. Use the sliders and input fields to configure the parameters for the effect.
5. Click the **"Apply Changes"** button. The "Edited Image" preview will update with the result.
6. Once you are satisfied, click the **"Download Edited Image"** button to save the file.

---

### 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

---

### 📧 Contact

MohammadReza Hasanzadeh - [mr.hk@aut.ac.ir] - [linkedin.com/in/cemrh]
