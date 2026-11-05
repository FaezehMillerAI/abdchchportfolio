# Dr. Abdolah Chalechale – Academic Portfolio & Interactive CV
> **دکتر عبدالله چاله چاله | پورتفولیو و رزومه علمی تعاملی**  
> Associate Professor of Computer Engineering & Artificial Intelligence, Razi University  
> دانشیار مهندسی کامپیوتر و هوش مصنوعی، دانشگاه رازی

[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-1400%2B%20Citations-4285F4?logo=google-scholar&logoColor=white)](https://scholar.google.com/citations?user=C1-FBkUAAAAJ&hl=en)
[![Razi University](https://img.shields.io/badge/Razi%20University-Faculty%20Profile-005696)](https://en.razi.ac.ir/~chalechale/home)
[![h-index](https://img.shields.io/badge/h--index-18-emerald)](https://scholar.google.com/citations?user=C1-FBkUAAAAJ&hl=en)
[![i10-index](https://img.shields.io/badge/i10--index-31-indigo)](https://scholar.google.com/citations?user=C1-FBkUAAAAJ&hl=en)
[![Bilingual](https://img.shields.io/badge/Language-English%20%7C%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-blue)](#)
[![Theme](https://img.shields.io/badge/Theme-Dark%20%2F%20Light-purple)](#)
[![Multi-Page Architecture](https://img.shields.io/badge/Structure-Multi--Page%20Clean-success)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Overview / درباره پروژه

This repository contains the interactive academic portfolio and digital Curriculum Vitae for **Dr. Abdolah Chalechale**. It features a **multi-page clean architecture** where each section has its own dedicated page with zero visual clutter:
- **Home (`index.html`)**: Executive summary, biography, key statistics, core research pillars, and recent 2024–2026 breakthroughs.
- **Publications (`publications.html`)**: Interactive publications hub with real-time search, category/topic filters, annual trajectory chart, and BibTeX/APA citation generators.
- **Theses & Students (`theses.html`)**: Directory of supervised M.Sc. and Ph.D. graduate research filterable by graduation year.
- **Academic Journey (`experience.html`)**: Visual timeline of education (Sharif B.Sc./M.Sc., Wollongong Ph.D.) and university leadership (15-year tenure as Head of Computing Center).
- **Teaching (`teaching.html`)**: Graduate and undergraduate curricula, course descriptions, and syllabi.
- **Patents & Projects (`projects.html`)**: Registered national patents and applied industrial research contracts.
- **Contact (`contact.html`)**: Academic office, direct contact information, and university portal access.

---

## ✨ Key Features / ویژگی‌های کلیدی

1. **🌐 Full Bilingual Support (دوزبانه کامل - انگلیسی و فارسی):**
   - Instant 1-click toggle between **English** and **Persian (فارسی)** across all pages.
   - Dynamic switching of document direction (`dir="rtl"` / `dir="ltr"`).
   - High-grade typography using Google's **Vazirmatn** for Persian and **Outfit / Plus Jakarta Sans** for English.
   - State persisted seamlessly via `localStorage`.

2. **🌓 Dark and Light Themes (حالت شب و روز):**
   - High-contrast, elegant dark theme with obsidian backdrop and indigo accents.
   - Clean, crisp light theme with ivory cards and deep navy typography.
   - Zero text overflow, clean alignment, and `white-space: nowrap` strictly enforced on all nav links and buttons.

3. **📑 Multi-Page Clean Architecture (صفحات مجزا برای هر تب):**
   - No cramped single-page scrolling; each tab navigates to a dedicated, spacious HTML page.
   - Fixed, perfectly proportioned navbar with no broken or multi-line stacked text.
   - Responsive mobile navigation drawer for smartphones and tablets.

4. **🔍 Interactive Publications & Research Hub:**
   - Real-time search across titles, authors, venues, years, and keywords.
   - Filter pills: All Works, Journal Articles, Conferences, Selected Highlights.
   - **One-click "Copy BibTeX" and "Copy APA"** citations with floating toast notifications.
   - Expandable abstract modal with DOI and publisher links.

5. **📊 Research Analytics & Trajectory Visualizer:**
   - Responsive vector SVG bar chart showing annual publication momentum (2002–2026).
   - Distribution progress bars detailing thematic contributions.

6. **🖨️ One-Click Print / PDF CV:**
   - Built-in `@media print` styling that transforms the website into a clean, distraction-free, print-perfect academic CV ready to save as PDF.

---

## 🚀 How to Run Locally / اجرای محلی

This project is built with **zero external dependencies or build tools** (pure modern HTML5, CSS3, and vanilla JavaScript).

### Option 1: Direct Browser Launch
Simply double-click `index.html` or open it with any web browser (Chrome, Firefox, Safari, Edge).

### Option 2: Python Local Server
```bash
python3 -m http.server 8000
# Open http://localhost:8000 in your browser
```

---

## 🌐 1-Click Deployment to GitHub Pages / انتشار در گیتهاب

1. **Create a GitHub Repository:**
   - Go to [GitHub](https://github.com/new) and create a repository (e.g. `chalechale`).
2. **Push the Files:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Dr. Abdolah Chalechale Multi-Page Portfolio"
   git branch -M main
   git remote add origin https://github.com/<YOUR-USERNAME>/<REPO-NAME>.git
   git push -u origin main
   ```
3. **Enable GitHub Pages:**
   - Go to your repository on GitHub: **Settings** -> **Pages**.
   - Under **Build and deployment** -> **Source**, select **Deploy from a branch**.
   - Under **Branch**, select `main` and folder `/ (root)`.
   - Click **Save**.
   - Within 1–2 minutes, your website will be live!

---

## 📁 Repository Structure / ساختار فایل‌ها

```
Resume/
├── index.html               # صفحه اصلی (Overview, Stats, Research Pillars)
├── publications.html        # صفحه اختصاصی مقالات علمی و پژوهشی
├── theses.html              # صفحه اختصاصی پایان‌نامه‌ها و دانش‌آموختگان
├── experience.html          # صفحه سوابق تحصیلی و مسئولیت‌های اجرایی
├── teaching.html            # صفحه دروس و آموزش دانشگاهی
├── projects.html            # صفحه ثبت اختراعات و طرح‌های کاربردی
├── contact.html             # صفحه تماس، دفتر کار و ارتباط با استاد
├── README.md                # مستندات و راهنمای انتشار
├── build_dataset.py         # اسکریپت استخراج و کامپایل اطلاعات
├── assets/
│   ├── css/
│   │   └── style.css        # استایل مدرن، ریسپانسیو، تم‌های شب/روز، استایل چاپ
│   ├── js/
│   │   ├── data.js          # دیتاست کامل دوزبانه مقالات، پایان‌نامه‌ها، دروس
│   │   └── app.js           # منطق کنترل‌کننده تعاملی، فیلترها، جستجو، تغییر زبان/تم
│   └── images/
│       └── profile.jpg      # عکس پرتره رسمی استاد (دانشگاه رازی)
└── رزومه چاله چاله.pdf       # فایل رزومه اولیه
```

---

## 👨‍🏫 About Dr. Abdolah Chalechale

- **Rank:** Associate Professor (دانشیار)
- **Institution:** Faculty of Engineering, Razi University, Kermanshah, Iran
- **Alma Mater:** University of Wollongong (Ph.D., 2005), Sharif University of Technology (B.Sc., 1991; M.Sc., 1994)
- **Citations:** 1,412+ | **h-index:** 18 | **i10-index:** 31
- **Email:** `chalechale@razi.ac.ir` | `a.chalechale@gmail.com`
- **Profiles:** [Google Scholar](https://scholar.google.com/citations?user=C1-FBkUAAAAJ&hl=en) · [Razi University (EN)](https://en.razi.ac.ir/~chalechale/home) · [Razi University (FA)](https://razi.ac.ir/~chalechale)

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
Designed with care and respect for Dr. Abdolah Chalechale.
