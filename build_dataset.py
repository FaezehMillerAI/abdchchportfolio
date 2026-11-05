# -*- coding: utf-8 -*-
"""
Compile comprehensive bilingual data for Dr. Abdolah Chalechale's Portfolio Website.
Sources:
  1. رزومه چاله چاله.pdf (OCR 33 pages)
  2. Razi University Portal (English & Persian) up to 2026
  3. Google Scholar metrics
"""

import json

profile = {
    "name": {
        "en": "Dr. Abdolah Chalechale",
        "fa": "دکتر عبدالله چاله چاله"
    },
    "title": {
        "en": "Associate Professor of Computer Engineering & Artificial Intelligence",
        "fa": "دانشیار مهندسی کامپیوتر و هوش مصنوعی"
    },
    "affiliation": {
        "en": "Faculty of Engineering, Razi University, Kermanshah, Iran",
        "fa": "دانشکده فنی و مهندسی، دانشگاه رازی، کرمانشاه، ایران"
    },
    "department": {
        "en": "Department of Computer Engineering and Information Technology",
        "fa": "گروه مهندسی کامپیوتر و فناوری اطلاعات"
    },
    "bio": {
        "en": "Dr. Abdolah Chalechale is an Associate Professor of Computer Engineering at Razi University. He earned his B.Sc. and M.Sc. in Electrical and Software Engineering from Sharif University of Technology, Tehran, and his Ph.D. in Artificial Intelligence and Digital Image Processing from the University of Wollongong, Australia (awarded the Iranian Government Scholarship). With over three decades of academic leadership—including 15 years as Head of the Computing & Internet Center and multiple terms as Department Head—his research pioneers advancements in Deep Learning, Medical Image Diagnosis (Pancreatic, Liver, CT/MRI, Biopsy), Natural Language Processing, Distributed Systems, Federated Learning, and Meta-heuristic Optimization. He has published over 100 journal and conference papers in top venues (IEEE, Springer, Elsevier) with more than 1,400 citations.",
        "fa": "دکتر عبدالله چاله چاله، دانشیار گروه مهندسی کامپیوتر و فناوری اطلاعات دانشگاه رازی است. ایشان مدرک کارشناسی و کارشناسی ارشد خود را در رشته‌های مهندسی برق و مهندسی نرم‌افزار از دانشگاه صنعتی شریف تهران و مدرک دکتری تخصصی خود را در زمینه هوش مصنوعی و پردازش تصاویر دیجیتال از دانشگاه ولونگونگ استرالیا (با بورس تحصیلی دولتی) اخذ نموده‌اند. با بیش از سه دهه سابقه درخشان در آموزش و مدیریت دانشگاهی — از جمله ۱۵ سال ریاست مرکز محاسبات و اینترنت دانشگاه رازی و چندین دوره مدیریت گروه مهندسی کامپیوتر — پژوهش‌های ایشان بر لبه فناوری در حوزه‌های یادگیری عمیق، پردازش تصاویر پزشکی (تشخیص سرطان پانکراس، کبد، سی‌تی‌اسکن و ام‌آر‌آی)، پردازش زبان طبیعی، سیستم‌های توزیع‌شده، یادگیری فدرال و الگوریتم‌های بهینه‌سازی فراابتکاری متمرکز است. حاصل فعالیت‌های علمی ایشان بیش از ۱۰۰ مقاله در نشریات و کنفرانس‌های معتبر بین‌المللی (IEEE، Springer، Elsevier)، ثبت اختراع، طرح‌های پژوهشی کاربردی و راهنمایی ده‌ها پایان‌نامه تحصیلات تکمیلی است."
    },
    "personal_quote": {
        "en": "\"I consider each and every one of my students as my own children, sparing no effort to guide them toward academic excellence and meaningful societal impact.\"",
        "fa": "«تک‌تک دانشجویانم را مثل فرزندان خودم می‌دانم و برای موفقیت و تعالی علمی آنها از هیچ تلاشی دریغ نمی‌ورزم.»"
    },
    "photo": "assets/images/profile.jpg",
    "email": "chalechale@razi.ac.ir",
    "phone": "+98 (83) 34343235",
    "office": {
        "en": "Faculty of Engineering, Razi University, Taq-e Bostan, Kermanshah, Iran",
        "fa": "کرمانشاه، طاق بستان، دانشگاه رازی، دانشکده فنی و مهندسی"
    },
    "scholar_url": "https://scholar.google.com/citations?user=C1-FBkUAAAAJ&hl=en",
    "razi_en_url": "https://en.razi.ac.ir/~chalechale/home",
    "razi_fa_url": "https://razi.ac.ir/~chalechale",
    "stats": {
        "citations": 1412,
        "recent_citations": 761,
        "h_index": 18,
        "recent_h_index": 14,
        "i10_index": 31,
        "recent_i10_index": 16,
        "publications_count": 110,
        "theses_count": 85,
        "experience_years": 32,
        "patents_count": 2,
        "projects_count": 7
    }
}

research_interests = [
    {
        "id": "ai_deeplearning",
        "title_en": "Artificial Intelligence & Deep Learning",
        "title_fa": "هوش مصنوعی و یادگیری عمیق",
        "icon": "brain",
        "desc_en": "CNN architectures, Vision Transformers, Generative Adversarial Networks (GANs), and multi-scale feature representation.",
        "desc_fa": "معماری‌های نوین CNN، ترنسفورمرهای بینایی، شبکه‌های مولد تخاصمی (GAN) و بازنمایی ویژگی‌های چندمقیاسی."
    },
    {
        "id": "medical_imaging",
        "title_en": "Medical Image Analysis & CAD",
        "title_fa": "پردازش تصاویر پزشکی و تشخیص رایانه‌ای",
        "icon": "heart-pulse",
        "desc_en": "3D CT/MRI analysis for pancreatic tumor classification, liver ultrasound segmentation, and histopathology stain translation.",
        "desc_fa": "پردازش سه‌بعدی CT/MRI برای تشخیص تومورهای پانکراس، بخش‌بندی سونوگرافی کبد و رنگ‌آمیزی تصاویر بافت‌آسیب‌شناسی."
    },
    {
        "id": "nlp_sentiment",
        "title_en": "Natural Language Processing (NLP)",
        "title_fa": "پردازش زبان طبیعی و تحلیل احساسات",
        "icon": "chat-quote",
        "desc_en": "Personality and emotion detection, Persian BERT language modeling, social network sentiment analysis, and transformer models.",
        "desc_fa": "تشخیص ابعاد شخصیت و احساسات، مدل‌سازی زبان فارسی با BERT، تحلیل احساسات شبکه‌های اجتماعی و مدل‌های ترنسفورمر."
    },
    {
        "id": "distributed_fog",
        "title_en": "Distributed Systems & Cloud-Fog Computing",
        "title_fa": "سیستم‌های توزیع‌شده و محاسبات مه-ابر",
        "icon": "cloud-network",
        "desc_en": "Federated learning client selection (DACS), deadline-aware load balancing, IoT task offloading, and autonomous vehicular fog.",
        "desc_fa": "انتخاب بهینه کلاینت در یادگیری فدرال (DACS)، توازن بار حساس به مهلت زمانی، تخلیه بار وظایف IoT و مه خودروهای خودمختار."
    },
    {
        "id": "optimization",
        "title_en": "Meta-heuristic Optimization",
        "title_fa": "الگوریتم‌های بهینه‌سازی فراابتکاری",
        "icon": "cpu",
        "desc_en": "Grasshopper optimization (GOA), Whale Optimization (WOA), and Chimp optimization applied to multi-level image thresholding and neural networks.",
        "desc_fa": "الگوریتم‌های ملخ (GOA)، نهنگ (WOA) و شامپانزه برای آستانه‌گذاری چندسطحی تصاویر و بهینه‌سازی شبکه‌های عصبی."
    },
    {
        "id": "biometrics_vision",
        "title_en": "Biometrics & Computer Vision",
        "title_fa": "بیومتریک، بینایی ماشین و بازشناسی الگو",
        "icon": "fingerprint",
        "desc_en": "Finger knuckle print & fingernail multi-modal biometric fusion, hand vein verification, signature analysis, and gesture-based HMI.",
        "desc_fa": "تلفیق ویژگی‌های بیومتریک بند انگشت و ناخن، شناسایی ورید دست، بازشناسی امضا و رابط‌های تعامل انسان و ماشین مبتنی بر ژست."
    }
]

education = [
    {
        "degree_en": "Ph.D. in Computer Engineering (Artificial Intelligence & Digital Image Processing)",
        "degree_fa": "دکتری تخصصی مهندسی کامپیوتر (هوش مصنوعی و پردازش تصاویر دیجیتال)",
        "institution_en": "University of Wollongong, New South Wales, Australia",
        "institution_fa": "دانشگاه ولونگونگ، استرالیا",
        "year": "2001 - 2005 (1380 - 1384)",
        "details_en": "Recipient of Iranian Government Doctoral Scholarship. Dissertation focused on innovative sketch-based image retrieval, angular partitioning, and contour description algorithms under supervision of renowned international scholars.",
        "details_fa": "اخذ مدرک با استفاده از بورس تحصیلی دولتی. رساله دکتری متمرکز بر بازیابی تصاویر مبتنی بر طرح‌های ترسیمی، افرازبندی زاویه‌ای و توصیف کانتورهای دیجیتال."
    },
    {
        "degree_en": "M.Sc. in Computer Engineering (Software Engineering)",
        "degree_fa": "کارشناسی ارشد مهندسی کامپیوتر (مهندسی نرم‌افزار)",
        "institution_en": "Sharif University of Technology, Tehran, Iran",
        "institution_fa": "دانشگاه صنعتی شریف، تهران، ایران",
        "year": "1992 - 1994 (1371 - 1373)",
        "details_en": "Graduated from Iran's premier engineering institute with focus on advanced algorithms, computer systems architecture, and distributed processing.",
        "details_fa": "فارغ‌التحصیل از برترین دانشگاه فنی و مهندسی کشور با تمرکز بر الگوریتم‌های پیشرفته، معماری سیستم‌های کامپیوتری و پردازش داده‌ها."
    },
    {
        "degree_en": "B.Sc. in Electrical Engineering (Electronics / Hardware)",
        "degree_fa": "کارشناسی مهندسی برق (الکترونیک / سخت‌افزار)",
        "institution_en": "Sharif University of Technology, Tehran, Iran",
        "institution_fa": "دانشگاه صنعتی شریف، تهران، ایران",
        "year": "1987 - 1992 (1366 - 1371)",
        "details_en": "Comprehensive training in digital logic design, microprocessors, electronic circuitry, and signal processing fundamentals.",
        "details_fa": "تحصیلات بنیادین در طراحی مدارات الکترونیک، سیستم‌های دیجیتال، ریزپردازنده‌ها و مبانی پردازش سیگنال."
    }
]

leadership = [
    {
        "role_en": "Head of Computing & Internet Center",
        "role_fa": "رئیس مرکز محاسبات و اینترنت دانشگاه رازی",
        "institution_en": "Razi University",
        "institution_fa": "دانشگاه رازی",
        "period": "1999 - 2014 (1378 - 1393)",
        "desc_en": "Led the university-wide ICT infrastructure development for 15 consecutive years. Pioneered the campus high-speed fiber-optic network, centralized student internet services, academic servers, and university data center.",
        "desc_fa": "مدیریت و هدایت کلان زیرساخت‌های فناوری اطلاعات و ارتباطات دانشگاه رازی به مدت ۱۵ سال مستمر. راه‌اندازی شبکه فیبر نوری پرسرعت پردیس، سرورهای محاسباتی، سامانه‌های دانشجویی و دیتاسنتر دانشگاه."
    },
    {
        "role_en": "Head of Computer Engineering Department",
        "role_fa": "مدیر گروه مهندسی کامپیوتر و فناوری اطلاعات",
        "institution_en": "Faculty of Engineering, Razi University",
        "institution_fa": "دانشکده فنی و مهندسی، دانشگاه رازی",
        "period": "1996 - 2018 (1375 - 1397)",
        "desc_en": "Served multiple terms leading curriculum modernization, launching graduate programs (M.Sc. and Ph.D. in Computer Engineering), recruiting faculty, and establishing specialized research laboratories.",
        "desc_fa": "هدایت چندین دوره مدیریت گروه، بازنگری و مدرن‌سازی سرفصل‌های درسی، راه‌اندازی دوره‌های کارشناسی ارشد و دکتری تخصصی، جذب اساتید نخبه و تجهیز آزمایشگاه‌های تخصصی کامپیوتر."
    },
    {
        "role_en": "Scientific Advisor, Student Computer Scientific Association",
        "role_fa": "استاد مشاور انجمن علمی دانشجویی مهندسی کامپیوتر",
        "institution_en": "Razi University",
        "institution_fa": "دانشگاه رازی",
        "period": "2006 - Present (1385 - اکنون)",
        "desc_en": "Mentoring student-led coding workshops, hackathons, national robotics and programming competitions, and research initiatives.",
        "desc_fa": "هدایت، مشاوره و پشتیبانی مستمر از فعالیت‌های علمی، کارگاه‌های تخصصی، مسابقات برنامه‌نویسی و المپیادهای علمی دانشجویان."
    }
]

courses = [
    {
        "id": "adv_os",
        "title_en": "Advanced Operating Systems",
        "title_fa": "سیستم‌های عامل پیشرفته",
        "level_en": "Graduate (M.Sc. / Ph.D.)",
        "level_fa": "تحصیلات تکمیلی (کارشناسی ارشد و دکتری)",
        "units": 3,
        "desc_en": "In-depth study of kernel design, multi-threading, concurrency control, distributed synchronization, memory virtualization, and hypervisors.",
        "desc_fa": "بررسی عمیق معماری هسته سیستم‌های عامل، همروندی، کنترل بن‌بست، همگام‌سازی توزیع‌شده، مجازی‌سازی حافظه و هایپروایزرها."
    },
    {
        "id": "distributed_systems",
        "title_en": "Distributed Systems",
        "title_fa": "سیستم‌های توزیع‌شده",
        "level_en": "Graduate (M.Sc.)",
        "level_fa": "کارشناسی ارشد",
        "units": 3,
        "desc_en": "Architectures, consensus protocols (Raft/Paxos), RPC, cloud/fog computing paradigms, federated learning coordination, and fault tolerance.",
        "desc_fa": "معماری سیستم‌های توزیع‌شده، پروتکل‌های اجماع، محاسبات مه و ابر، هماهنگی در یادگیری فدرال و تحمل‌پذیری در برابر خطا."
    },
    {
        "id": "digital_image_processing",
        "title_en": "Digital Image Processing",
        "title_fa": "پردازش تصاویر دیجیتال",
        "level_en": "Undergraduate & Graduate",
        "level_fa": "کارشناسی و کارشناسی ارشد",
        "units": 3,
        "desc_en": "Spatial and frequency domain filtering, image restoration, morphological analysis, edge detection, segmentation, and feature extraction.",
        "desc_fa": "فیلترگذاری در حوزه‌های مکان و فرکانس، بازیابی تصویر، پردازش‌های مورفولوژیک، تشخیص لبه، بخش‌بندی و استخراج ویژگی."
    },
    {
        "id": "ai_foundations",
        "title_en": "Artificial Intelligence",
        "title_fa": "هوش مصنوعی",
        "level_en": "Undergraduate",
        "level_fa": "کارشناسی",
        "units": 3,
        "desc_en": "State-space search strategies, heuristic search, game playing, propositional logic, inference engines, and knowledge representation.",
        "desc_fa": "جستجوهای فضای حالت، الگوریتم‌های هیوریستیک، تئوری بازی‌ها، منطق گزاره‌ای و مرتبه اول، موتورهای استنتاج و بازنمایی دانش."
    },
    {
        "id": "ann",
        "title_en": "Artificial Neural Networks & Deep Learning",
        "title_fa": "شبکه‌های عصبی مصنوعی و یادگیری عمیق",
        "level_en": "Graduate (M.Sc. / Ph.D.)",
        "level_fa": "کارشناسی ارشد و دکتری",
        "units": 3,
        "desc_en": "Perceptrons, backpropagation, MLP, convolutional neural networks (CNN), recurrent architectures (LSTM/GRU), and regularized optimization.",
        "desc_fa": "پرسپترون، پس‌انتشار خطا، شبکه‌های پیچشی عمیق (CNN)، شبکه‌های بازگشتی (LSTM/GRU) و روش‌های بهینه‌سازی یادگیری."
    },
    {
        "id": "sp_eng",
        "title_en": "Specialized English for Computer Engineers",
        "title_fa": "زبان تخصصی مهندسی کامپیوتر",
        "level_en": "Undergraduate",
        "level_fa": "کارشناسی",
        "units": 2,
        "desc_en": "Technical academic terminology, scientific paper drafting, reading comprehension of IEEE/ACM literature, and oral scientific presentation skills.",
        "desc_fa": "اصطلاحات تخصصی فناوری، نگارش مقالات علمی، درک متون تخصصی IEEE/ACM و مهارت‌های ارائه شفاهی سمینارهای علمی."
    }
]

patents = [
    {
        "id": "pat_1",
        "title_en": "Image Processing Digital Counter Device for Utility Meters",
        "title_fa": "دستگاه پردازش تصویر مخصوص کنتور و شمارنده‌های دیجیتالی",
        "patent_no": "2992 / 1390",
        "year": "2011 (1390)",
        "inventors_en": "Abdolah Chalechale, Alireza Amini Sardari, Nader Karimi Tahneh",
        "inventors_fa": "عبدالله چاله چاله، علیرضا امینی سرداری، نادر کریمی طهنه",
        "type_en": "National Patent (State Organization for Registration of Deeds and Properties)",
        "type_fa": "ثبت اختراع رسمی (سازمان ثبت اسناد و املاک کشور)",
        "desc_en": "An automated optical character and digit reading device for mechanical and electronic utility meters (water, electricity, gas) using embedded computer vision algorithms for tamper-proof remote meter logging.",
        "desc_fa": "سامانه خودکار قرائت اپتیکی ارقام کنتورهای مکانیکی و الکترونیکی با استفاده از الگوریتم‌های پردازش تصویر تعبیه‌شده جهت قرائت از راه دور و جلوگیری از دستکاری."
    },
    {
        "id": "pat_2",
        "title_en": "Embedded Cardless Purchase Terminal System",
        "title_fa": "دستگاه تعبیه‌شده خرید بدون نیاز به کارت اعتباری",
        "patent_no": "1389",
        "year": "2010 (1389)",
        "inventors_en": "Abdolah Chalechale",
        "inventors_fa": "عبدالله چاله چاله",
        "type_en": "National Patent",
        "type_fa": "ثبت اختراع رسمی",
        "desc_en": "Innovative secure embedded hardware terminal enabling electronic financial transactions and authentication without physical credit/debit card presentation.",
        "desc_fa": "سامانه سخت‌افزاری تعبیه‌شده امن برای پردازش و انجام تراکنش‌های خرید الکترونیکی بدون نیاز به همراه داشتن فیزیکی کارت بانکی."
    }
]

applied_projects = [
    {
        "id": "proj_1",
        "title_en": "Stereo Vision Indoor Mapping for Autonomous Goalkeeper Robot",
        "title_fa": "تعیین نقشه تقریبی یک محیط بسته با بکارگیری دید استریو و کاربرد آن در بینایی روبات دروازه‌بان",
        "sponsor_en": "Applied Industrial Research Grant",
        "sponsor_fa": "طرح پژوهشی کاربردی",
        "year": "2011 - 2012 (1390 - 1391)",
        "role_en": "Principal Investigator",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "Developed real-time stereo disparity mapping and 3D depth triangulation for autonomous robot navigation and ball interception.",
        "desc_fa": "طراحی و پیاده‌سازی نگاشت استریو و مثلث‌بندی سه‌بعدی برای ناوبری بلادرنگ و واکنش سریع روبات دروازه‌بان در محیط بسته."
    },
    {
        "id": "proj_2",
        "title_en": "Strategic IT Roadmaps for Industrial Energy Consumption Reduction",
        "title_fa": "تعیین راهکارهای استفاده از فناوری اطلاعات در کاهش مصرف انرژی",
        "sponsor_en": "Ministry of Energy / Regional Power Corporation",
        "sponsor_fa": "طرح پژوهشی - شرکت توزیع نیروی برق",
        "year": "2011 - 2012 (1390 - 1391)",
        "role_en": "Principal Investigator",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "Formulated intelligent algorithms and IoT-based monitoring protocols to optimize energy distribution and reduce electrical grid loads.",
        "desc_fa": "طراحی راهکارهای مبتنی بر فناوری اطلاعات و الگوریتم‌های هوشمند جهت پایش، کنترل بار و بهینه‌سازی مصرف انرژی در شبکه."
    },
    {
        "id": "proj_3",
        "title_en": "Enterprise CAD & Spatial Croquis Management Software Suite",
        "title_fa": "سیستم نرم‌افزار مدیریت کروکی‌های اجرایی",
        "sponsor_en": "Telecommunications & Urban Utilities Organization",
        "sponsor_fa": "طرح توسعه‌ای کاربردی",
        "year": "2010 - 2012 (1389 - 1391)",
        "role_en": "Project Director",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "A GIS-integrated vector drafting and indexing management platform for surveying engineers and utility network infrastructure.",
        "desc_fa": "توسعه نرم‌افزار جامع مدیریت، ترسیم و بایگانی هوشمند کروکی‌های اجرایی و نقشه‌های شبکه‌های شهری با قابلیت تلفیق GIS."
    },
    {
        "id": "proj_4",
        "title_en": "Biometric Identity Verification using Finger Knuckle and Fingernail Imaging",
        "title_fa": "تشخیص هویت بیومتریک با استفاده از تصاویر پنجه و ناخن",
        "sponsor_en": "National Research Grant",
        "sponsor_fa": "طرح پژوهشی مصوب",
        "year": "2009 - 2010 (1388 - 1389)",
        "role_en": "Principal Investigator",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "Designed novel texture and geometric descriptors for contact-free multi-biometric human identity verification.",
        "desc_fa": "طراحی توصیف‌گرهای نوین بافت و ساختار هندسی بند انگشت و ناخن جهت احراز هویت بیومتریک بدون تماس فیزیکی."
    },
    {
        "id": "proj_5",
        "title_en": "Electronic Client-Servicing System (Laboratory & Semi-Industrial Prototype)",
        "title_fa": "تحقیق و پیاده‌سازی نمونه آزمایشگاهی و نیمه‌صنعتی سیستم تکریم الکترونیکی ارباب رجوع",
        "sponsor_en": "Government Administrative Reform Organization",
        "sponsor_fa": "طرح پژوهشی کاربردی",
        "year": "2008 (1387)",
        "role_en": "Principal Investigator",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "Engineered an automated kiosk and workflow queuing platform providing citizens with transparent case tracking and service evaluation.",
        "desc_fa": "طراحی و ساخت کیوسک و نرم‌افزار تعاملی نوبت‌دهی هوشمند و رهگیری برخط فرایندهای اداری ارباب رجوع."
    },
    {
        "id": "proj_6",
        "title_en": "Automated Coin Recognition and Valuation via Computer Vision",
        "title_fa": "شناسایی و تفکیک خودکار سکه‌ها با استفاده از روش‌های پردازش تصویر",
        "sponsor_en": "Applied Industry Research",
        "sponsor_fa": "طرح پژوهشی کاربردی",
        "year": "2007 - 2010 (1386 - 1389)",
        "role_en": "Principal Investigator",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "Developed high-speed circular edge extraction and relief pattern matching algorithms for automated commercial currency sorters.",
        "desc_fa": "توسعه الگوریتم‌های سریع استخراج لبه‌های دایروی و تطبیق الگوهای برجسته سکه جهت دستگاه‌های سورتر تجاری."
    },
    {
        "id": "proj_7",
        "title_en": "Human Body Gesture Recognition for Visual Human-Computer Interaction",
        "title_fa": "بررسی روش‌های تشخیص حرکات بدن به منظور ارتباطات دیداری با کامپیوتر",
        "sponsor_en": "Foundational Research Initiative",
        "sponsor_fa": "طرح پژوهشی بنیادی-کاربردی",
        "year": "2003 - 2006 (1382 - 1385)",
        "role_en": "Principal Investigator",
        "role_fa": "مجری اصلی: دکتر عبدالله چاله چاله",
        "desc_en": "Explored markerless human gesture segmentation and dynamic posture classification for next-generation touchless interfaces.",
        "desc_fa": "تحلیل حرکات و وضعیت بدن انسان بدون نیاز به نشانگر برای ایجاد رابط‌های کاربری تعاملی نسل جدید."
    }
]

# Comprehensive Publications Collection (Journals & Conferences)
publications = [
    {
        "id": "pub_2026_1",
        "category": "journal",
        "year": 2026,
        "title_en": "An improved grasshopper optimization algorithm for multilevel thresholding image segmentation",
        "title_fa": "الگوریتم بهبود‌یافته بهینه‌سازی ملخ برای آستانه‌گذاری چندسطحی در بخش‌بندی تصاویر",
        "authors": "Leila Amiri, Abdolah Chalechale, Maryam Taghizadeh",
        "journal_en": "International Journal of Nonlinear Analysis and Applications",
        "journal_fa": "مجله بین‌المللی تحلیل غیرخطی و کاربردها",
        "publisher": "IJNAA",
        "topic": "optimization",
        "highlight": True,
        "badge": "2026 Latest",
        "abstract_en": "Proposes an enhanced meta-heuristic Grasshopper Optimization Algorithm (GOA) integrated with chaotic maps and adaptive operators to achieve optimal multi-level threshold selection for challenging natural and medical image segmentation tasks.",
        "abstract_fa": "ارائه نسخه ارتقایافته الگوریتم بهینه‌سازی ملخ (GOA) همراه با نگاشت‌های آشوبناک و عملگرهای تطبیقی جهت تعیین بهینه آستانه‌های چندسطحی در بخش‌بندی تصاویر طبیعی و پزشکی."
    },
    {
        "id": "pub_2026_2",
        "category": "journal",
        "year": 2026,
        "title_en": "DACS: Deadline-Aware Adaptive Client Selection in federated learning",
        "title_fa": "DACS: انتخاب تطبیقی و آگاه از مهلت زمانی کلاینت‌ها در یادگیری فدرال",
        "authors": "Aref Arefnia, Abdolah Chalechale",
        "journal_en": "Cluster Computing - The Journal of Networks, Software Tools and Applications",
        "journal_fa": "مجله محاسبات خوشه‌ای (اسپرینگر)",
        "publisher": "Springer",
        "topic": "distributed_fog",
        "highlight": True,
        "badge": "Springer Q1",
        "pages": "1-18",
        "doi": "10.1007/s10586-026-x",
        "abstract_en": "Federated learning across heterogeneous edge nodes often suffers from straggler clients. This paper introduces DACS, a deadline-aware client selection mechanism that adaptively schedules edge participants to maximize model accuracy while strictly respecting training latency deadlines.",
        "abstract_fa": "در یادگیری فدرال بر روی گره‌های ناهمگن لبه، کلاینت‌های کند عملکرد کل سیستم را مختل می‌کنند. این مقاله چارچوب DACS را معرفی می‌کند که با در نظر گرفتن مهلت زمانی و ظرفیت محاسباتی، مشارکت‌کنندگان را به گونه‌ای انتخاب می‌کند که دقت مدل بیشینه و محدودیت زمان رعایت گردد."
    },
    {
        "id": "pub_2026_3",
        "category": "journal",
        "year": 2026,
        "title_en": "Optimized-based load balancing in a hybrid cloud-fog architecture",
        "title_fa": "توازن بار مبتنی بر بهینه‌سازی در معماری ترکیبی ابر و مه",
        "authors": "Saif Obaid Hussein, Abdolah Chalechale, Maryam Taghizadeh",
        "journal_en": "The Journal of Supercomputing",
        "journal_fa": "مجله ابرمحاسبات (اسپرینگر)",
        "publisher": "Springer",
        "topic": "distributed_fog",
        "highlight": True,
        "badge": "Springer Q1",
        "pages": "1-25",
        "abstract_en": "Presents an intelligent bio-inspired load balancing framework specifically formulated for tiered Cloud-Fog infrastructures, significantly cutting service delay, network congestion, and energy costs for latency-critical IoT tasks.",
        "abstract_fa": "ارائه چارچوب هوشمند توازن بار با الهام از الگوریتم‌های زیستی برای معماری‌های سلسله‌مراتبی مه-ابر که منجر به کاهش چشمگیر تاخیر سرویس، بار ترافیکی شبکه و مصرف انرژی در پردازش وظایف بلادرنگ اینترنت اشیاء می‌شود."
    },
    {
        "id": "pub_2024_1",
        "category": "journal",
        "year": 2024,
        "title_en": "A deep learning-based and adaptive region proposal algorithm for semantic segmentation",
        "title_fa": "الگوریتم تطبیقی و مبتنی بر یادگیری عمیق پیشنهاد ناحیه برای بخش‌بندی معنایی",
        "authors": "Maryam Taghizadeh, Abdolah Chalechale",
        "journal_en": "Applied Soft Computing",
        "journal_fa": "محاسبات نرم کاربردی (الزویر)",
        "publisher": "Elsevier",
        "topic": "ai_deeplearning",
        "highlight": True,
        "badge": "Elsevier Q1",
        "abstract_en": "Introduces an adaptive region proposal generation framework that leverages hierarchical multi-scale feature maps from convolutional networks, substantially outperforming traditional selective search and edge boxes in recall and IoU on benchmark datasets.",
        "abstract_fa": "معرفی الگوریتم تطبیقی تولید پیشنهاد ناحیه با بهره‌گیری از نقشه‌های ویژگی سلسله‌مراتبی شبکه‌های کانولوشنی، که برتری قابل توجهی نسبت به روش‌های سنتی Selective Search و Edge Boxes در معیار Recall و همپوشانی IoU ثبت کرده است."
    },
    {
        "id": "pub_2023_1",
        "category": "journal",
        "year": 2023,
        "title_en": "Emotion and personality analysis and detection using natural language processing, advances, challenges and future scope",
        "title_fa": "تحلیل و تشخیص احساسات و شخصیت با استفاده از پردازش زبان طبیعی: پیشرفت‌ها، چالش‌ها و چشم‌انداز آینده",
        "authors": "Faezeh Safari, Abdolah Chalechale",
        "journal_en": "Artificial Intelligence Review",
        "journal_fa": "نشریه مروری بر هوش مصنوعی (اسپرینگر)",
        "publisher": "Springer",
        "topic": "nlp_sentiment",
        "highlight": True,
        "badge": "Springer Q1 (IF ~12)",
        "doi": "10.1007/s10462-023-10495-2",
        "abstract_en": "A premier comprehensive survey analyzing state-of-the-art computational methods in emotion and personality trait modeling from textual modalities. Evaluates transformer architectures (BERT, RoBERTa, GPT), benchmark datasets, multi-modal alignment, and privacy challenges.",
        "abstract_fa": "یک مقاله مروری جامع و پیشرو در ارزیابی روش‌های محاسباتی نوین استخراج ابعاد شخصیت و احساسات از داده‌های متنی. بررسی ترنسفورمرهای مدرن، دیتاست‌های مرجع، تطبیق چندحالتی و چالش‌های حریم خصوصی در سیستم‌های هوشمند."
    },
    {
        "id": "pub_2023_2",
        "category": "journal",
        "year": 2023,
        "title_en": "A new gated multi-scale convolutional neural network architecture for recognition of Persian handwritten texts",
        "title_fa": "معماری جدید شبکه عصبی پیچشی چندمقیاسی دریچه‌دار جهت بازشناسی متون دست‌نویس فارسی",
        "authors": "Sara Khosravi, Abdolah Chalechale",
        "journal_en": "International Journal of Nonlinear Analysis and Applications",
        "journal_fa": "مجله بین‌المللی تحلیل غیرخطی و کاربردها",
        "publisher": "IJNAA",
        "topic": "ai_deeplearning",
        "highlight": False,
        "abstract_en": "Designs a gated multi-scale receptive field mechanism inside CNN blocks to capture intricate cursive stroke dependencies and diacritical marks in Persian and Arabic handwritten manuscripts.",
        "abstract_fa": "طراحی مکانیزم ناحیه پذیرش چندمقیاسی مجهز به گیت در بلوک‌های CNN جهت درک پیوستگی کلمات و نشانه‌های خط دست‌نویس فارسی و عربی با دقت بسیار بالا."
    },
    {
        "id": "pub_2022_1",
        "category": "journal",
        "year": 2022,
        "title_en": "A Hybrid Indoor Positioning Model for Critical Situations Based on Localization Technologies",
        "title_fa": "مدل موقعیت‌یابی ترکیبی فضای بسته برای شرایط بحرانی بر اساس فناوری‌های مکان‌یابی",
        "authors": "Alaa Abdulhussein Mahdi, Abdolah Chalechale, Ashraf AbdelRaouf",
        "journal_en": "Mobile Information Systems",
        "journal_fa": "سیستم‌های اطلاعاتی سیار (وایلی/هنداوی)",
        "publisher": "Hindawi / Wiley",
        "topic": "distributed_fog",
        "pages": "1-15",
        "doi": "10.1155/2022/9431872",
        "abstract_en": "Develops a fault-tolerant indoor positioning paradigm integrating Wi-Fi fingerprinting, BLE beacons, and pedestrian dead reckoning (PDR) to ensure continuous tracking for first responders during structural crises.",
        "abstract_fa": "طراحی مدل مکان‌یابی داخلی مقاوم در برابر خطا با تلفیق اثرانگشت Wi-Fi، بیکن‌های BLE و ناوبری عابر پیاده (PDR) جهت هدایت نیروهای امدادی در شرایط بحرانی."
    },
    {
        "id": "pub_2022_2",
        "category": "journal",
        "year": 2022,
        "title_en": "Median arc center corrected binary pattern (MACCBP) for noise robust feature extraction",
        "title_fa": "الگوی دودویی تصحیح‌شده مرکز قوس میانه (MACCBP) برای استخراج ویژگی‌های مقاوم به نویز",
        "authors": "Sayed Mohammad Tabatabaei, Abdolah Chalechale",
        "journal_en": "Multidimensional Systems and Signal Processing",
        "journal_fa": "سیستم‌های چندبعدی و پردازش سیگنال (اسپرینگر)",
        "publisher": "Springer",
        "topic": "biometrics_vision",
        "badge": "Springer",
        "pages": "1409-1444",
        "abstract_en": "Formulates the MACCBP texture descriptor which overcomes classical Local Binary Pattern (LBP) vulnerabilities under heavy Gaussian and salt-and-pepper noise regimes in facial and surface classification.",
        "abstract_fa": "ابداع توصیف‌گر بافت MACCBP که ضعف‌های کلاسیک الگوی محلی دودویی (LBP) را در شرایط نویز شدید گوسی و فلفل-نمکی در بازشناسی چهره و بافت به طور کامل برطرف می‌سازد."
    },
    {
        "id": "pub_2022_3",
        "category": "journal",
        "year": 2022,
        "title_en": "An Efficient Hybrid Model Based on Modified Whale Optimization Algorithm and Multilayer Perceptron Neural Network for Medical Classification Problems",
        "title_fa": "مدل ترکیبی کارآمد بر اساس الگوریتم اصلاح‌شده بهینه‌سازی نهنگ و شبکه عصبی پرسپترون برای مسائل رده‌بندی پزشکی",
        "authors": "Saeid Raziani, Sajad Ahmadian, Seyed Mohammad Jafar Jalali, Abdolah Chalechale",
        "journal_en": "Journal of Bionic Engineering",
        "journal_fa": "نشریه مهندسی بیونیک (اسپرینگر)",
        "publisher": "Springer",
        "topic": "medical_imaging",
        "badge": "Springer Q1",
        "pages": "1504-1521",
        "abstract_en": "Integrates an enhanced Whale Optimization Algorithm (WOA) with multi-layer perceptron training to avoid local minima trap, demonstrated on cardiovascular, diabetes, and breast cancer diagnostic callsets.",
        "abstract_fa": "ترکیب الگوریتم بهینه‌سازی اصلاح‌شده نهنگ با شبکه عصبی پرسپترون چندلایه جهت فرار از بهینه‌های محلی در تشخیص بیماری‌های قلبی-عروقی، دیابت و سرطان سینه."
    },
    {
        "id": "pub_2022_4",
        "category": "journal",
        "year": 2022,
        "title_en": "A comprehensive and systematic review on classical and deep learning based region proposal algorithms",
        "title_fa": "مرور جامع و سیستماتیک بر الگوریتم‌های پیشنهاد ناحیه کلاسیک و مبتنی بر یادگیری عمیق",
        "authors": "Maryam Taghizadeh, Abdolah Chalechale",
        "journal_en": "Expert Systems with Applications",
        "journal_fa": "سیستم‌های خبره با کاربردها (الزویر)",
        "publisher": "Elsevier",
        "topic": "ai_deeplearning",
        "highlight": True,
        "badge": "Elsevier Q1",
        "pages": "116105",
        "abstract_en": "A cornerstone review critically examining over 100 region proposal methodologies spanning grouping methods, window scoring, and modern deep region proposal networks (RPNs), offering standardized benchmarks.",
        "abstract_fa": "بررسی جامع و سیستماتیک بیش از ۱۰۰ الگوریتم تولید پیشنهاد ناحیه از روش‌های سنتی گروه‌بندی تا شبکه‌های عمیق RPN، همراه با تحلیل مقایسه‌ای نقاط قوت و ضعف بر روی دیتاست‌های معیار."
    },
    {
        "id": "pub_2022_5",
        "category": "journal",
        "year": 2022,
        "title_en": "Biometric authentication using a deep learning approach based on different level fusion of finger knuckle print and fingernail",
        "title_fa": "احراز هویت بیومتریک با رویکرد یادگیری عمیق بر پایه تلفیق سطوح مختلف اثر بند انگشت و ناخن",
        "authors": "Hadis Heidari, Abdolah Chalechale",
        "journal_en": "Expert Systems with Applications",
        "journal_fa": "سیستم‌های خبره با کاربردها (الزویر)",
        "publisher": "Elsevier",
        "topic": "biometrics_vision",
        "highlight": True,
        "badge": "Elsevier Q1",
        "pages": "116443",
        "abstract_en": "Proposes a multi-modal biometric framework fusing finger knuckle patterns and dorsal fingernail textures via deep convolutional feature extractors and score-level fusion, achieving near-zero equal error rates.",
        "abstract_fa": "معرفی سامانه بیومتریک چندحالتی با ترکیب ویژگی‌های بافت بند انگشت و ناخن با استفاده از شبکه‌های عمیق کانولوشنی و تلفیق در سطح امتیاز، با دستیابی به خطای نزدیک به صفر."
    },
    {
        "id": "pub_2022_6",
        "category": "journal",
        "year": 2022,
        "title_en": "Chimp optimization algorithm to optimize a convolutional neural network for recognizing Persian/Arabic handwritten words",
        "title_fa": "الگوریتم بهینه‌سازی شامپانزه جهت تنظیم بهینه شبکه عصبی کانولوشنی در بازشناسی کلمات دست‌نویس فارسی/عربی",
        "authors": "Sara Khosravi, Abdolah Chalechale",
        "journal_en": "Mathematical Problems in Engineering",
        "journal_fa": "مسائل ریاضی در مهندسی",
        "publisher": "Hindawi",
        "topic": "ai_deeplearning",
        "pages": "1-12",
        "abstract_en": "Applies the bio-inspired Chimp Optimization Algorithm (ChOA) to hyper-parameter tuning and filter weights optimization in CNNs, setting new state-of-the-art accuracy on Iranian handwritten benchmarks.",
        "abstract_fa": "بکارگیری الگوریتم بهینه‌سازی شامپانزه در تنظیم ابرپارامترها و وزن‌های فیلترهای شبکه عصبی عمیق جهت بازشناسی کلمات دست‌نویس فارسی با دقت رکوردشکن."
    },
    {
        "id": "pub_2021_1",
        "category": "journal",
        "year": 2021,
        "title_en": "An efficient cardiovascular disease detection model based on multilayer perceptron and moth-flame optimization",
        "title_fa": "مدل کارآمد تشخیص بیماری‌های قلبی-عروقی بر پایه پرسپترون چندلایه و الگوریتم پروانه-شعله",
        "authors": "Sajad Ahmadian, Seyed Mohammad Jafar Jalali, Saeid Raziani, Abdolah Chalechale",
        "journal_en": "Expert Systems",
        "journal_fa": "سیستم‌های خبره (وایلی)",
        "publisher": "Wiley",
        "topic": "medical_imaging",
        "badge": "Wiley",
        "abstract_en": "Formulates an automated cardiac diagnostic model coupling MLP neural networks with Moth-Flame Optimization (MFO) to identify subtle electrocardiographic anomalies.",
        "abstract_fa": "طراحی مدل خودکار تشخیص نارسایی‌های قلبی با ترکیب شبکه عصبی پرسپترون و الگوریتم بهینه‌سازی پروانه-شعله جهت شناسایی ناهنجاری‌های پنهان داده‌های بالینی."
    },
    {
        "id": "pub_2021_2",
        "category": "journal",
        "year": 2021,
        "title_en": "Improving IoT Services Using a Hybrid Fog-Cloud Offloading",
        "title_fa": "ارتقای سرویس‌های اینترنت اشیاء با استفاده از تخلیه بار محاسباتی ترکیبی مه و ابر",
        "authors": "Saif Obaid Hussein, Abdolah Chalechale",
        "journal_en": "IEEE Access",
        "journal_fa": "دسترسی آزاد IEEE",
        "publisher": "IEEE",
        "topic": "distributed_fog",
        "badge": "IEEE",
        "pages": "13775-13788",
        "abstract_en": "An optimization strategy balancing execution latency and device battery life across mobile edge gateways and cloud servers for smart city IoT deployments.",
        "abstract_fa": "راهکار بهینه‌سازی توزیع بار محاسباتی با ایجاد تعادل بهینه بین تاخیر اجرا و طول عمر باتری تجهیزات اینترنت اشیاء بین گره‌های مه و سرورهای ابری."
    },
    {
        "id": "pub_2021_3",
        "category": "journal",
        "year": 2021,
        "title_en": "A class-independent flexible algorithm to generate region proposals",
        "title_fa": "الگوریتم منعطف و مستقل از کلاس برای تولید پیشنهادهای ناحیه",
        "authors": "Maryam Taghizadeh, Abdolah Chalechale",
        "journal_en": "Multimedia Tools and Applications",
        "journal_fa": "ابزارها و کاربردهای چندرسانه‌ای (اسپرینگر)",
        "publisher": "Springer",
        "topic": "ai_deeplearning",
        "pages": "31737-31758",
        "abstract_en": "Presents an unsupervised perceptual grouping strategy extracting high-quality bounding proposals for object localization without class-specific training priors.",
        "abstract_fa": "معرفی روش ادراک بصری بدون نظارت برای استخراج پیشنهادهای باکیفیت مکان‌یابی اشیا در تصاویر، مستقل از دسته‌بندی و بدون نیاز به آموزش پیشین."
    },
    {
        "id": "pub_2020_1",
        "category": "journal",
        "year": 2020,
        "title_en": "A new biometric identity recognition system based on a combination of superior features in finger knuckle print images",
        "title_fa": "سیستم جدید شناسایی هویت بیومتریک مبتنی بر ترکیب ویژگی‌های برتر در تصاویر بند انگشت",
        "authors": "Hadis Heidari, Abdolah Chalechale",
        "journal_en": "Turkish Journal of Electrical Engineering and Computer Sciences",
        "journal_fa": "نشریه مهندسی برق و علوم کامپیوتر ترکیه",
        "publisher": "TUBITAK",
        "topic": "biometrics_vision",
        "pages": "238-252",
        "abstract_en": "Combines radon transform projections and bandpass Gabor filters to extract distinctive orientation ridge lines from finger knuckle skin folds.",
        "abstract_fa": "ترکیب تبدیل رادون و فیلترهای گابور جهتی جهت استخراج الگوهای منحصر‌به‌فرد خطوط پوست بند انگشت در کاربردهای امنیتی و هویتی."
    },
    {
        "id": "pub_2019_1",
        "category": "journal",
        "year": 2019,
        "title_en": "Noise-tolerant texture feature extraction through directional thresholded local binary pattern",
        "title_fa": "استخراج ویژگی بافت مقاوم به نویز از طریق الگوی محلی دودویی آستانه‌گذاری‌شده جهتی",
        "authors": "Sayed Mohammad Tabatabaei, Abdolah Chalechale",
        "journal_en": "The Visual Computer",
        "journal_fa": "رایانه بصری (اسپرینگر)",
        "publisher": "Springer",
        "topic": "biometrics_vision",
        "pages": "1581-1598",
        "abstract_en": "Formulates directional gradient offsets ensuring stable texture classification even under severe salt-and-pepper, speckle, and illumination variations.",
        "abstract_fa": "فرمولاسیون گرادیان‌های جهتی برای تضمین پایداری شناسایی بافت در شرایط نویز شدید، تغییرات شدید روشنایی و اعوجاج تصاویر."
    },
    {
        "id": "pub_2018_1",
        "category": "journal",
        "year": 2018,
        "title_en": "Energy Consumption Improvement and Cost Saving by Cloud Broker in Cloud Datacenters",
        "title_fa": "بهبود مصرف انرژی و کاهش هزینه با استفاده از کارگزار ابری در مراکز داده",
        "authors": "A. Karamolahy, Abdolah Chalechale, Mahmoud Ahmadi",
        "journal_en": "International Arab Journal of Information Technology (IAJIT)",
        "journal_fa": "مجله بین‌المللی فناوری اطلاعات جهان عرب",
        "publisher": "IAJIT",
        "topic": "distributed_fog",
        "pages": "405-411",
        "abstract_en": "Presents an intelligent broker framework dynamically allocating virtual machines across physical servers to maximize sleep states and slash datacenter electric overhead.",
        "abstract_fa": "ارائه چارچوب کارگزار ابری هوشمند جهت تخصیص پویای ماشین‌های مجازی به سرورهای فیزیکی با هدف بهینه‌سازی مصرف برق مراکز داده."
    },
    {
        "id": "pub_2014_1",
        "category": "journal",
        "year": 2014,
        "title_en": "Parallel Implementation of Color Based Image Retrieval Using CUDA on the GPU",
        "title_fa": "پیاده‌سازی موازی بازیابی تصویر مبتنی بر رنگ با استفاده از CUDA بر روی پردازنده گرافیکی",
        "authors": "Hadis Heidari, Abdolah Chalechale, AliReza Ahmadi",
        "journal_en": "International Journal of Information Technology and Computer Science (IJITCS)",
        "journal_fa": "نشریه بین‌المللی فناوری اطلاعات و علوم کامپیوتر",
        "publisher": "MECS",
        "topic": "biometrics_vision",
        "abstract_en": "Leverages GPU massively parallel SIMD thread blocks to accelerate multi-dimensional color histogram extraction and Euclidean distance querying by up to 45x.",
        "abstract_fa": "بهره‌گیری از هسته‌های موازی کارت‌های گرافیک انویدیا با CUDA جهت شتاب‌بخشی ۴۵ برابری به استخراج هیستوگرام رنگ و جستجوی شباهت در پایگاه داده‌های تصویری حجیم."
    },
    {
        "id": "pub_2005_1",
        "category": "journal",
        "year": 2005,
        "title_en": "Sketch-based image matching using angular partitioning",
        "title_fa": "تطبیق تصاویر مبتنی بر طرح‌های ترسیمی با استفاده از افرازبندی زاویه‌ای",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Alfred Mertins",
        "journal_en": "IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics)",
        "journal_fa": "تراکنش‌های IEEE در سیستم‌ها، انسان و سایبرنتیک",
        "publisher": "IEEE",
        "topic": "biometrics_vision",
        "highlight": True,
        "badge": "IEEE Trans (Flagship)",
        "pages": "1059-1065",
        "abstract_en": "Seminal doctoral research publication presenting Angular Radial Partitioning (ARP). Enables invariant sketch-to-image matching resistant to scale, rotation, and translation, becoming a foundational citation in content-based image retrieval (CBIR).",
        "abstract_fa": "مقاله برجسته و بنیادین رساله دکتری در IEEE Transactions که روش افرازبندی زاویه‌ای-شعاعی (ARP) را ابداع نمود. این روش امکان بازیابی تصاویر از روی اسکچ دست‌نویس با مقاومت در برابر چرخش، مقیاس و انتقال را فراهم کرد و به یکی از مراجع پرتکرار مقالات بین‌المللی تبدیل شد."
    },
    {
        "id": "pub_2004_1",
        "category": "journal",
        "year": 2004,
        "title_en": "Edge image description using angular radial partitioning",
        "title_fa": "توصیف تصویر لبه با استفاده از افرازبندی زاویه‌ای-شعاعی",
        "authors": "Abdolah Chalechale, Alfred Mertins, Golshah Naghdy",
        "journal_en": "IEE Proceedings - Vision, Image and Signal Processing",
        "journal_fa": "مجموعه مقالات IEE - بینایی، تصویر و پردازش سیگنال",
        "publisher": "IEE / IET",
        "topic": "biometrics_vision",
        "badge": "IEE / IET",
        "pages": "93-98",
        "abstract_en": "Establishes harmonic decomposition principles across polar sectors of binary edge maps, providing compact feature signatures for MPEG-7 visual shape descriptors.",
        "abstract_fa": "ارائه اصول تجزیه هارمونیک در قطاع‌های قطبی تصاویر لبه جهت تولید توصیف‌گرهای فشرده و کارآمد با استاندارد بین‌المللی MPEG-7."
    },
    {
        "id": "pub_2004_2",
        "category": "journal",
        "year": 2004,
        "title_en": "Sketch-based shape retrieval using length and curvature of 2D digital contours",
        "title_fa": "بازیابی شکل مبتنی بر اسکچ با استفاده از طول و انحنای کانتورهای دیجیتال دو بعدی",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Prashan Premaratne",
        "journal_en": "Lecture Notes in Computer Science (LNCS)",
        "journal_fa": "درس‌نامه‌های علوم کامپیوتر (اشپرینگر)",
        "publisher": "Springer LNCS",
        "topic": "biometrics_vision",
        "badge": "Springer LNCS",
        "volume": "3322",
        "abstract_en": "Formulates contour differential curvature profiles to match hand-drawn contour fragments against high-resolution object silhouettes.",
        "abstract_fa": "فرمولاسیون انحنای دیفرانسیلی کانتور برای تطبیق قطعات منحنی رسم‌شده با دست با سایه‌نماهای اجسام در بانک‌های تصویر دیجیتال."
    },
    {
        "id": "pub_2002_1",
        "category": "journal",
        "year": 2002,
        "title_en": "An abstract image representation based on edge pixel neighborhood information (EPNI)",
        "title_fa": "بازنمایی انتزاعی تصویر بر اساس اطلاعات همسایگی پیکسل‌های لبه (EPNI)",
        "authors": "Abdolah Chalechale, Alfred Mertins",
        "journal_en": "Lecture Notes in Computer Science (LNCS)",
        "journal_fa": "درس‌نامه‌های علوم کامپیوتر (اشپرینگر)",
        "publisher": "Springer LNCS",
        "topic": "biometrics_vision",
        "badge": "Springer LNCS",
        "volume": "2525",
        "abstract_en": "Introduces EPNI: a spatial co-occurrence histogram capturing directional structural density in abstract line drawings and artistic sketches.",
        "abstract_fa": "معرفی روش EPNI: ماتریس هیستوگرام فضایی چگالی ساختاری جهت بازنمایی انتزاعی نقاشی‌ها و طرح‌های خطی."
    },
    # Selected High-Profile International & National Conferences
    {
        "id": "conf_1",
        "category": "conference",
        "year": 2024,
        "title_en": "Semantic Segmentation Using Region Proposals and Weakly-Supervised Learning",
        "title_fa": "بخش‌بندی معنایی با استفاده از پیشنهادهای ناحیه و یادگیری با نظارت ضعیف",
        "authors": "Maryam Taghizadeh, Abdolah Chalechale",
        "conference_en": "12th International Conference on Computer and Knowledge Engineering (ICCKE)",
        "conference_fa": "دوازدهمین کنفرانس بین‌المللی مهندسی کامپیوتر و دانش",
        "location": "Mashhad, Iran",
        "topic": "ai_deeplearning"
    },
    {
        "id": "conf_2",
        "category": "conference",
        "year": 2023,
        "title_en": "Classification of Personality Traits on Facebook Using Key Phrase Extraction, Language Models and Machine Learning",
        "title_fa": "رده‌بندی ویژگی‌های شخصیتی در فیسبوک با استخراج عبارات کلیدی، مدل‌های زبانی و یادگیری ماشین",
        "authors": "Faezeh Safari, Abdolah Chalechale",
        "conference_en": "13th International Conference on Information and Knowledge Technology (IKT)",
        "conference_fa": "سیزدهمین کنفرانس بین‌المللی فناوری اطلاعات و دانش",
        "location": "Tehran, Iran",
        "topic": "nlp_sentiment"
    },
    {
        "id": "conf_3",
        "category": "conference",
        "year": 2023,
        "title_en": "An overview of the methods of diagnosing oral and dental diseases using image processing and deep learning techniques",
        "title_fa": "مروری بر روش‌های تشخیص بیماری‌های دهان و دندان با پردازش تصویر و یادگیری عمیق",
        "authors": "Fatemeh Mahmoodi, Abdolah Chalechale, Faezeh Safari",
        "conference_en": "1st International Conference on Information Technology, Management and Computer",
        "conference_fa": "اولین کنفرانس بین‌المللی فناوری اطلاعات، مدیریت و کامپیوتر",
        "location": "Tehran, Iran",
        "topic": "medical_imaging"
    },
    {
        "id": "conf_4",
        "category": "conference",
        "year": 2022,
        "title_en": "Traffic Captioning: Deep Learning-based Method to Understand and Describe Traffic Images",
        "title_fa": "تولید خودکار شرح تصاویر ترافیکی بر پایه یادگیری عمیق",
        "authors": "Parniya Seifi, Abdolah Chalechale",
        "conference_en": "8th International Conference on Signal Processing and Intelligent Systems (ICSPIS)",
        "conference_fa": "هشتمین کنفرانس بین‌المللی پردازش سیگنال و سیستم‌های هوشمند",
        "location": "Tehran, Iran",
        "topic": "ai_deeplearning"
    },
    {
        "id": "conf_5",
        "category": "conference",
        "year": 2020,
        "title_en": "Region Proposal Generation: A Hierarchical Merging Similarity-Based Algorithm",
        "title_fa": "تولید پیشنهاد ناحیه: الگوریتمی بر پایه ادغام سلسله‌مراتبی شباهت",
        "authors": "Maryam Taghizadeh, Abdolah Chalechale",
        "conference_en": "11th Iranian Machine Vision and Image Processing Conference (MVIP)",
        "conference_fa": "یازدهمین کنفرانس بینایی ماشین و پردازش تصویر ایران",
        "location": "Tehran, Iran",
        "topic": "ai_deeplearning"
    },
    {
        "id": "conf_6",
        "category": "conference",
        "year": 2016,
        "title_en": "Classification of Iranian Paintings Using Texture Analysis and Machine Learning",
        "title_fa": "رده‌بندی سبک نقاشی‌های ایرانی با استفاده از تحلیل بافت و یادگیری ماشین",
        "authors": "Sanaz Keshvari, Abdolah Chalechale",
        "conference_en": "6th International Conference on Computer and Knowledge Engineering (ICCKE)",
        "conference_fa": "ششمین کنفرانس بین‌المللی مهندسی کامپیوتر و دانش",
        "location": "Mashhad, Iran",
        "topic": "biometrics_vision"
    },
    {
        "id": "conf_7",
        "category": "conference",
        "year": 2004,
        "title_en": "Image database retrieval using sketched queries",
        "title_fa": "بازیابی در پایگاه داده تصاویر با استفاده از پرس‌وجوهای اسکچ",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Prashan Premaratne",
        "conference_en": "IEEE International Conference on Image Processing (ICIP 2004)",
        "conference_fa": "کنفرانس بین‌المللی پردازش تصویر IEEE (سنگاپور)",
        "location": "Singapore",
        "badge": "IEEE ICIP (Flagship)",
        "topic": "biometrics_vision"
    },
    {
        "id": "conf_8",
        "category": "conference",
        "year": 2004,
        "title_en": "Document image analysis and verification using cursive signature",
        "title_fa": "تحلیل و اعتبارسنجی تصاویر اسناد با استفاده از امضای پیوسته",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Prashan Premaratne, Alfred Mertins",
        "conference_en": "IEEE International Conference on Multimedia and Expo (ICME 2004)",
        "conference_fa": "کنفرانس بین‌المللی چندرسانه‌ای IEEE (تایوان)",
        "location": "Taipei, Taiwan",
        "badge": "IEEE ICME",
        "topic": "biometrics_vision"
    },
    {
        "id": "conf_9",
        "category": "conference",
        "year": 2004,
        "title_en": "Angular-radial decomposition algorithm for sketch-based image retrieval",
        "title_fa": "الگوریتم تجزیه زاویه‌ای-شعاعی برای بازیابی تصاویر مبتنی بر اسکچ",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Prashan Premaratne, Alfred Mertins",
        "conference_en": "8th World Multi-Conference on Systemics, Cybernetics and Informatics (WMSCI)",
        "conference_fa": "هشتمین کنفرانس جهانی سیستمیک، سایبرنتیک و انفورماتیک (فلوریدا)",
        "location": "Orlando, Florida, USA",
        "topic": "biometrics_vision"
    },
    {
        "id": "conf_10",
        "category": "conference",
        "year": 2003,
        "title_en": "Signature-based document retrieval",
        "title_fa": "بازیابی اسناد بر مبنای امضا",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Alfred Mertins",
        "conference_en": "3rd IEEE International Symposium on Signal Processing and Information Technology (ISSPIT)",
        "conference_fa": "سومین سمپوزیوم بین‌المللی پردازش سیگنال IEEE (آلمان)",
        "location": "Darmstadt, Germany",
        "badge": "IEEE ISSPIT",
        "topic": "biometrics_vision"
    },
    {
        "id": "conf_11",
        "category": "conference",
        "year": 2003,
        "title_en": "Visual investigation using circular partitioning of abstract images",
        "title_fa": "بررسی بصری با افرازبندی دایروی تصاویر انتزاعی",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Alfred Mertins",
        "conference_en": "7th International Conference on Digital Image Computing Techniques and Applications (DICTA)",
        "conference_fa": "هفتمین کنفرانس پردازش تصویر دیجیتال استرالیا (سیدنی)",
        "location": "Sydney, Australia",
        "badge": "DICTA Australia",
        "topic": "biometrics_vision"
    },
    {
        "id": "conf_12",
        "category": "conference",
        "year": 2005,
        "title_en": "Hand gesture selection and recognition for visual-based human-machine interface",
        "title_fa": "انتخاب و بازشناسی ژست‌های دست برای رابط تعاملی انسان و ماشین",
        "authors": "Abdolah Chalechale, Golshah Naghdy, Prashan Premaratne",
        "conference_en": "IEEE Electro/Information Technology Conference",
        "conference_fa": "کنفرانس الکترونیک و فناوری اطلاعات IEEE (آمریکا)",
        "location": "Nebraska, USA",
        "badge": "IEEE EIT",
        "topic": "biometrics_vision"
    }
]

# Supervised Graduate Theses (Selected High-Impact Cohort)
theses = [
    {
        "id": "th_2026_1",
        "year": 2026,
        "degree": "M.Sc.",
        "student_en": "Mosa Ibrahim Hammoodi",
        "student_fa": "موسی ابراهیم حمودی",
        "title_en": "Computer-Aided Diagnosis of Pancreas Diseases from Medical Imaging Using Convolutional Neural Networks",
        "title_fa": "تشخیص رایانه‌ای بیماری‌های پانکراس از تصاویر پزشکی با استفاده از شبکه‌های عصبی پیچشی عمیق",
        "domain": "medical_imaging",
        "abstract_en": "End-to-end 3D DenseNet121 architecture for binary classification (normal vs. pancreatic tumor) on 3D volumetric CT scans. Incorporates HU windowing, weighted cross-entropy for class imbalance, calibration via Brier score / ECE, and visual explainability via Grad-CAM.",
        "abstract_fa": "طراحی خط‌لوله کامل سه‌بعدی DenseNet121 برای رده‌بندی تومورهای بدخیم پانکراس در سی‌تی‌اسکن‌های حجمی با استفاده از تکنیک‌های هوش مصنوعی تفسیرپذیر (Grad-CAM) و بهینه‌سازی آستانه یودن."
    },
    {
        "id": "th_2026_2",
        "year": 2026,
        "degree": "M.Sc.",
        "student_en": "Pezhman Najafi",
        "student_fa": "پژمان نجفی",
        "title_en": "Design and Implementation of Web-Based Software Using AI Models for Diagnosing and Describing Liver Disease Images",
        "title_fa": "طراحی و پیاده‌سازی نرم‌افزار تحت وب مبتنی بر مدل‌های هوش مصنوعی جهت تشخیص و توصیف تصاویر بیماری‌های کبدی",
        "domain": "medical_imaging",
        "abstract_en": "Created MultiBranch-AHCTNet combining Haralick texture features and deep representations for multi-stage liver fibrosis classification and automated clinical report generation.",
        "abstract_fa": "توسعه معماری MultiBranch-AHCTNet برای تشخیص مراحل فیبروز کبدی از روی سونوگرافی و تولید برخط گزارش پزشکی هوشمند."
    },
    {
        "id": "th_2026_3",
        "year": 2026,
        "degree": "M.Sc.",
        "student_en": "Ali Mohsin Abbood",
        "student_fa": "علی محسن عبود",
        "title_en": "Interpretable Hybrid Microscopic Biopsy Subtyping via Morphology-Texture Feature Fusion and Lightweight ML",
        "title_fa": "دسته‌بندی تفسیری بیوپسی‌های میکروسکوپی از طریق تلفیق ویژگی‌های مورفولوژی-بافت و یادگیری ماشین سبک‌وزن",
        "domain": "medical_imaging",
        "abstract_en": "Clinical histopathology decision support extracting cellular morphometrics and GLCM textures with SHAP value explainability.",
        "abstract_fa": "سامانه پشتیبان تصمیم‌گیری بالینی پاتولوژی با تلفیق ویژگی‌های ساختاری سلول و بافت با قابلیت تفسیرپذیری به روش SHAP."
    },
    {
        "id": "th_2026_4",
        "year": 2026,
        "degree": "M.Sc.",
        "student_en": "Hayder Mohammed Baqer Murad",
        "student_fa": "حیدر محمد باقر مراد",
        "title_en": "Automated Detection of Blood Patterns on Microscope Slides for Integrated Biopsy Diagnosis",
        "title_fa": "تشخیص خودکار الگوهای خونی بر روی لام‌های میکروسکوپی جهت تشخیص یکپارچه بیوپسی",
        "domain": "medical_imaging",
        "abstract_en": "Quality grading of peripheral blood smears across Raabin-WBC and BCCD datasets utilizing CLAHE enhancement and random forest classification.",
        "abstract_fa": "ارزیابی خودکار کیفیت گسترش خون محیطی و تفکیک سلول‌های خونی بر روی دیتاست‌های Raabin و BCCD."
    },
    {
        "id": "th_2026_5",
        "year": 2026,
        "degree": "M.Sc.",
        "student_en": "Hasanain Taha Shaalan",
        "student_fa": "حس Just حسنین طه شعلان",
        "title_en": "Automatic Osteoporosis Detection from Chest X-Ray (CXR) Images Using Deep Learning",
        "title_fa": "تشخیص خودکار پوکی استخوان از روی تصاویر رادیوگرافی قفسه سینه (CXR) با استفاده از یادگیری عمیق",
        "domain": "medical_imaging",
        "abstract_en": "Opportunistic osteoporosis screening from standard chest radiographs using DenseNet-121, providing affordable early fracture prevention.",
        "abstract_fa": "غربالگری زودهنگام پوکی استخوان از روی عکس‌های متداول رادیوگرافی قفسه سینه با شبکه DenseNet-121 بدون هزینه مازاد اسکن دانسیتومتری."
    },
    {
        "id": "th_2026_6",
        "year": 2026,
        "degree": "M.Sc.",
        "student_en": "Fatemeh Khalvandi",
        "student_fa": "فاطمه خلوندی",
        "title_en": "Diagnosis of Alzheimer's Disease Using Artificial Intelligence Techniques",
        "title_fa": "تشخیص بیماری آلزایمر با بکارگیری تکنیک‌های هوش مصنوعی",
        "domain": "medical_imaging",
        "abstract_en": "Early cognitive impairment detection from structural brain MRI biomarkers using convolutional neural networks.",
        "abstract_fa": "تشخیص زودهنگام اختلالات شناختی و آلزایمر از روی بیومارکرهای ام‌آر‌آی ساختاری مغز."
    },
    {
        "id": "th_2025_1",
        "year": 2025,
        "degree": "M.Sc.",
        "student_en": "Atefeh Darabi Ghasemi",
        "student_fa": "عاطفه دارابی قاسمی",
        "title_en": "Text-Based Sentiment Analysis Using Persian Natural Language Processing and Deep Learning",
        "title_fa": "تحلیل احساسات مبتنی بر متن با استفاده از پردازش زبان طبیعی فارسی و یادگیری عمیق",
        "domain": "nlp_sentiment",
        "abstract_en": "Fine-tuning Persian Bert-fa and Transformer models to detect customer polarity, sarcasm, and intent on Persian social media.",
        "abstract_fa": "تنظیم دقیق مدل‌های BERT زبان فارسی (ParsBERT) جهت استخراج قطبیت احساسات و کنایه‌های کلامی در شبکه‌های اجتماعی."
    },
    {
        "id": "th_2025_2",
        "year": 2025,
        "degree": "M.Sc.",
        "student_en": "Mohammadreza Bolvardi",
        "student_fa": "محمدرضا بولوردی",
        "title_en": "Emotion Recognition from Speech Signal Based on Deep Learning Methods",
        "title_fa": "تشخیص احساسات از سیگنال گفتار مبتنی بر روش‌های یادگیری عمیق",
        "domain": "nlp_sentiment",
        "abstract_en": "Combines Bi-LSTM temporal networks and acoustic spectral features (MFCCs, Chromagram) achieving 88% accuracy across EmoDB and SAVEE.",
        "abstract_fa": "ترکیب شبکه‌های دوطرفه Bi-LSTM و ویژگی‌های فرکانسی MFCC سیگنال صوتی جهت تشخیص هیجانات خشم، شادی و غم در گفتار."
    },
    {
        "id": "th_2025_3",
        "year": 2025,
        "degree": "M.Sc.",
        "student_en": "Amir Hossein Shahrokhi",
        "student_fa": "امیرحسین شاهرخی",
        "title_en": "An Intrusion Detection System Based on Hierarchical Federated Learning in Internet of Medical Things",
        "title_fa": "سیستم تشخیص نفوذ مبتنی بر یادگیری فدرال سلسله‌مراتبی در اینترنت اشیاء پزشکی (IoMT)",
        "domain": "distributed_fog",
        "abstract_en": "Privacy-preserving threat detection across connected hospital devices using local on-device updates and secure aggregation.",
        "abstract_fa": "حفظ حریم خصوصی داده‌های بیماران با پایش امنیتی توزیع‌شده و یادگیری فدرال در تجهیزات بیمارستانی متصل به اینترنت."
    },
    {
        "id": "th_2025_4",
        "year": 2025,
        "degree": "M.Sc.",
        "student_en": "Mohammadhadi Akbarzadeh",
        "student_fa": "محمدهادی اکبرزاده",
        "title_en": "Multi-Fog Computing Resource Allocation Management in Autonomous Vehicles",
        "title_fa": "مدیریت تخصیص منابع در محاسبات چندمهی برای خودروهای خودران",
        "domain": "distributed_fog",
        "abstract_en": "Reinforcement learning for vehicular edge task scheduling, cutting offload latencies during dense urban traffic maneuvers.",
        "abstract_fa": "تخصیص هوشمند منابع پردازشی به خودروهای خودران با یادگیری تقویتی در لایه‌های مه ترافیکی."
    },
    {
        "id": "th_2024_1",
        "year": 2024,
        "degree": "M.Sc.",
        "student_en": "Omid Mohammadi",
        "student_fa": "امید محمدی",
        "title_en": "Intelligent Similarity of Judicial Decisions and Laws Using Natural Language Processing Techniques",
        "title_fa": "بررسی شباهت هوشمند آراء قضایی و قوانین با تکنیک‌های پردازش زبان طبیعی",
        "domain": "nlp_sentiment",
        "abstract_en": "Semantic matching of Iranian legal court verdicts and statutory articles utilizing legal embedding representations.",
        "abstract_fa": "سامانه بازیابی و تطبیق معنایی هوشمند دادنامه‌های قضایی با مواد قانونی با استفاده از تعبیه‌سازی زبانی متون حقوقی."
    },
    {
        "id": "th_2023_1",
        "year": 2023,
        "degree": "M.Sc.",
        "student_en": "Hadis Rashno",
        "student_fa": "حدیث رشنو",
        "title_en": "Diagnosis of Brain Tumors Using the Combination of Meta-Heuristic Algorithms and Clustering Protocols in MRI Images",
        "title_fa": "تشخیص تومورهای مغزی با تلفیق الگوریتم‌های فراابتکاری و پروتکل‌های خوشه‌بندی در تصاویر MRI",
        "domain": "medical_imaging",
        "abstract_en": "Precise glioblastoma boundary extraction on BraTS2018 datasets using hybrid Coyote optimization and fuzzy clustering.",
        "abstract_fa": "جداسازی دقیق مرزهای تومور گلیوبلاستوما در تصاویر تشدید مغناطیسی با بهینه‌سازی ترکیبی و خوشه‌بندی فازی."
    },
    {
        "id": "th_2023_2",
        "year": 2023,
        "degree": "M.Sc.",
        "student_en": "Vahid Amiri",
        "student_fa": "وحید امیری",
        "title_en": "Sentiment Analysis in the Social Twitter Network with the Focus on Cryptocurrencies Using Machine Learning",
        "title_fa": "تحلیل احساسات در شبکه اجتماعی توییتر با تمرکز بر رمزارزها با استفاده از یادگیری ماشین",
        "domain": "nlp_sentiment",
        "abstract_en": "Real-time sentiment polarity indexing from financial tweets to forecast high-volatility cryptocurrency market fluctuations.",
        "abstract_fa": "استخراج نبض احساسی معامله‌گران در توییتر جهت پیش‌بینی نوسانات قیمتی بازار بیت‌کوین و اتریوم با یادگیری ماشین."
    },
    {
        "id": "th_2022_1",
        "year": 2022,
        "degree": "M.Sc.",
        "student_en": "Faezeh Safari",
        "student_fa": "فائزه صفری",
        "title_en": "Text-Based Personality Prediction Using Language Modeling and Deep Learning",
        "title_fa": "پیش‌بینی شخصیت مبتنی بر متن با استفاده از مدل‌سازی زبانی و یادگیری عمیق",
        "domain": "nlp_sentiment",
        "abstract_en": "Predicts Big Five personality traits from textual writings using SentenceTransformers, Longformer, and lexical linguistic inquiry models.",
        "abstract_fa": "پیش‌بینی پنج بعد اصلی شخصیت (Big Five) از روی متون نوشتاری با استفاده از SentenceTransformers و یادگیری عمیق چندمقیاسی."
    },
    {
        "id": "th_2022_2",
        "year": 2022,
        "degree": "M.Sc.",
        "student_en": "Parniya Seifi",
        "student_fa": "پرنیا سیفی",
        "title_en": "Semantic Captioning in Traffic Images Using Deep Learning",
        "title_fa": "توصیف و تولید شرح معنایی تصاویر ترافیکی با استفاده از یادگیری عمیق",
        "domain": "ai_deeplearning",
        "abstract_en": "Vision-language attention model generating descriptive text summaries for complex urban vehicular scenes.",
        "abstract_fa": "مدل توجه بصری-زبانی جهت تولید جملات توصیفی خودکار از رخدادها و تخلفات ترافیکی."
    },
    {
        "id": "th_2021_1",
        "year": 2021,
        "degree": "M.Sc.",
        "student_en": "Leila Amiri",
        "student_fa": "لیلا امیری",
        "title_en": "Evaluation and Optimization of Evolutionary Algorithms to Segment Natural Images",
        "title_fa": "ارزیابی و بهینه‌سازی الگوریتم‌های تکاملی در بخش‌بندی تصاویر طبیعی",
        "domain": "optimization",
        "abstract_en": "Benchmark study enhancing the Grasshopper Optimization Algorithm for fast Otsu and Kapur entropy thresholding.",
        "abstract_fa": "ارتقای الگوریتم بهینه‌سازی ملخ جهت بخش‌بندی سریع با معیارهای آنتروپی کاپور و اتسو."
    },
    {
        "id": "th_2020_1",
        "year": 2020,
        "degree": "M.Sc.",
        "student_en": "Pegah Salehi",
        "student_fa": "پگاه صالحی",
        "title_en": "Staining Histopathology Images Using Generative Adversarial Networks (GANs)",
        "title_fa": "رنگ‌آمیزی تصاویر بافت آسیب‌شناسی با استفاده از شبکه‌های مولد تخاصمی (GAN)",
        "domain": "medical_imaging",
        "abstract_en": "Conditional Pix2Pix GAN model for stain-to-stain normalization and virtual H&E histological dye transfer.",
        "abstract_fa": "نرمال‌سازی رنگ و انتقال مجازی رنگ‌آمیزی H&E در تصاویر آسیب‌شناسی با شبکه‌های مولد تخاصمی شرطی (Pix2Pix)."
    },
    {
        "id": "th_2017_1",
        "year": 2017,
        "degree": "M.Sc.",
        "student_en": "Farkhondeh Aryan Far",
        "student_fa": "فرخنده آرین فر",
        "title_en": "Parkinson's Disease Diagnosis via Online Handwriting Pattern Analysis",
        "title_fa": "تشخیص بیماری پارکینسون با تحلیل الگوهای دست‌نویس برخط",
        "domain": "medical_imaging",
        "abstract_en": "Detects micro-tremor kinetic anomalies in digital pen stroke speed, acceleration, and pressure.",
        "abstract_fa": "شناسایی لرزش‌های ریز پنهان در سرعت، شتاب و فشار قلم دیجیتال جهت تشخیص زودهنگام بیماری پارکینسون."
    },
    {
        "id": "th_2016_1",
        "year": 2016,
        "degree": "M.Sc.",
        "student_en": "Sanaz Keshvari",
        "student_fa": "ساناز کشوری",
        "title_en": "Stylometry and Forgery Detection in Iranian & Classical Paintings",
        "title_fa": "سبک‌سنجی و تشخیص اصالت در آثار نگارگری و نقاشی‌های کلاسیک",
        "domain": "biometrics_vision",
        "abstract_en": "Wavelet and texture brushstroke profiling to authenticate historical artworks and identify artist school styles.",
        "abstract_fa": "تحلیل ضربات قلم‌مو با تبدیل موجک برای تشخیص اصالت نقاشی‌های سنتی ایران و سبک‌شناسی خودکار."
    },
    {
        "id": "th_2014_1",
        "year": 2014,
        "degree": "M.Sc.",
        "student_en": "Hadis Heidari",
        "student_fa": "حدیث حیدری",
        "title_en": "Parallel Implementation of Color-Based Image Retrieval Using CUDA on the GPU",
        "title_fa": "پیاده‌سازی موازی بازیابی تصاویر بر اساس رنگ با CUDA بر روی کارت گرافیک",
        "domain": "biometrics_vision",
        "abstract_en": "Accelerating real-time massive multimedia search queries on NVIDIA Tesla GPU architectures.",
        "abstract_fa": "شتاب‌بخشی پردازش‌های حجیم جستجوی تصویر با معماری موازی کارت‌های گرافیک انویدیا."
    }
]


# Additional Classical Publications (2013-2018)
publications.extend([
    {
        'id': 'pub_2018_2',
        'category': 'journal',
        'year': 2018,
        'title_en': 'Local binary patterns for noise-tolerant sEMG classification',
        'title_fa': 'الگوهای دودویی محلی برای رده‌بندی سیگنال‌های الکترومایوگرافی سطحی (sEMG) مقاوم به نویز',
        'authors': 'Sayed Mohammad Tabatabaei, Abdolah Chalechale',
        'journal_en': 'Signal, Image and Video Processing',
        'journal_fa': 'پردازش سیگنال، تصویر و ویدیو (اسپرینگر)',
        'publisher': 'Springer',
        'topic': 'biometrics_vision',
        'pages': '1579-1587',
        'abstract_en': 'Presents a 1D variant of Local Binary Patterns to decode surface electromyographic signals for prosthetic hand controllers.',
        'abstract_fa': 'ارائه نسخه تک‌بعدی الگوی محلی دودویی جهت رمزگشایی سیگنال‌های عضلانی دست در پروتزهای هوشمند.'
    },
    {
        'id': 'pub_2016_1',
        'category': 'journal',
        'year': 2016,
        'title_en': 'An Evolutionary Stochastic Approach for Efficient Image Retrieval using Modified Particle Swarm Optimization',
        'title_fa': 'رویکرد تصادفی تکاملی برای بازیابی کارآمد تصاویر با بهینه‌سازی ازدحام ذرات اصلاح‌شده',
        'authors': 'Hadis Heidari, Abdolah Chalechale',
        'journal_en': 'International Journal of Advanced Computer Science and Applications (IJACSA)',
        'journal_fa': 'نشریه بین‌المللی علوم کامپیوتر پیشرفته',
        'publisher': 'IJACSA',
        'topic': 'optimization',
        'pages': '105-112',
        'abstract_en': 'Integrates PSO exploration with spatial color descriptors to minimize feature space dimensionality in large image archives.',
        'abstract_fa': 'تلفیق جستجوی تکاملی PSO با توصیف‌گرهای رنگی جهت کاهش ابعاد فضای ویژگی در پایگاه‌های داده تصویری.'
    },
    {
        'id': 'pub_2013_1',
        'category': 'journal',
        'year': 2013,
        'title_en': 'Persian Sign Language Recognition Using Radial Distance and Fourier Transform',
        'title_fa': 'بازشناسی زبان اشاره فارسی با استفاده از فاصله شعاعی و تبدیل فوریه',
        'authors': 'Bahare Jalilian, Abdolah Chalechale',
        'journal_en': 'International Journal of Image, Graphics and Signal Processing (IJIGSP)',
        'journal_fa': 'نشریه پردازش سیگنال و گرافیک تصویر',
        'publisher': 'MECS',
        'topic': 'biometrics_vision',
        'abstract_en': 'A vision-based Persian sign language interpreter extracting rotation-invariant contour radial vectors and Fourier coefficients.',
        'abstract_fa': 'سیستم ترجمه خودکار زبان اشاره فارسی بر اساس بردار فواصل شعاعی کانتور دست و ضرایب فوریه بدون وابستگی به زاویه چرخش.'
    },
    {
        'id': 'pub_2013_2',
        'category': 'journal',
        'year': 2013,
        'title_en': 'Hybrid PSO and Genetic Algorithm for Multilevel Maximum Entropy Criterion Threshold Selection',
        'title_fa': 'الگوریتم ترکیبی PSO و ژنتیک برای تعیین آستانه با معیار بیشینه آنتروپی در سطوح چندگانه',
        'authors': 'Esmaeil Akbari Banyani, Abdolah Chalechale',
        'journal_en': 'International Journal of Hybrid Information Technology (IJHIT)',
        'journal_fa': 'نشریه بین‌المللی فناوری اطلاعات ترکیبی',
        'publisher': 'SERSC',
        'topic': 'optimization',
        'pages': '131-140',
        'abstract_en': 'Combines genetic crossover diversity with PSO convergence speed to rapidly locate multi-threshold Kapur entropy cutoff levels.',
        'abstract_fa': 'ترکیب الگوریتم ژنتیک و PSO جهت تعیین پرسرعت آستانه‌های برش آنتروپی کاپور در بخش‌بندی تصاویر.'
    },
    {
        'id': 'pub_2013_3',
        'category': 'journal',
        'year': 2013,
        'title_en': 'Parallel implementation of texture based image retrieval on the GPU',
        'title_fa': 'پیاده‌سازی موازی بازیابی تصاویر مبتنی بر بافت بر روی پردازنده گرافیکی',
        'authors': 'Hadis Heidari, Abdolah Chalechale, AliReza Ahmadi',
        'journal_en': 'International Journal of Image, Graphics and Signal Processing (IJIGSP)',
        'journal_fa': 'نشریه بین‌المللی پردازش سیگنال و گرافیک تصویر',
        'publisher': 'MECS',
        'topic': 'biometrics_vision',
        'abstract_en': 'Massive multi-threaded Gabor wavelets implementation with NVIDIA CUDA yielding up to 38x speedup in texture classification.',
        'abstract_fa': 'پیاده‌سازی چندهسته‌ای موجک‌های گابور با معماری CUDA انویدیا جهت تسریع ۳۸ برابری در رده‌بندی بافت.'
    }
])

# Additional Historical Theses (2013-2019)
theses.extend([
    {
        'id': 'th_2019_1',
        'year': 2019,
        'degree': 'M.Sc.',
        'student_en': 'Fatemeh Rostambeigi',
        'student_fa': 'فاطمه رستم‌بیگی',
        'title_en': 'Voice Activity Detection Using Deep and Spectral Features in Noisy Environments',
        'title_fa': 'تشخیص فعالیت صوت با استفاده از ویژگی‌های عمیق و طیفی در محیط‌های نویزی',
        'domain': 'nlp_sentiment',
        'abstract_en': 'Speech endpoint boundary detection under severe acoustic noise using spectral centroid dynamics and neural networks.',
        'abstract_fa': 'تشخیص دقیق مرزهای گفتار انسان در محیط‌های پر سر و صدا با ترکیب مشخصه‌های دینامیک طیفی و شبکه‌های عصبی.'
    },
    {
        'id': 'th_2018_1',
        'year': 2018,
        'degree': 'M.Sc.',
        'student_en': 'Saeid Raziani',
        'student_fa': 'سعید رازیانی',
        'title_en': 'Design of Mobile Attendance Tracking System Based on Facial Recognition and GPS Geofencing',
        'title_fa': 'طراحی سیستم حضور و غیاب موبایل بر پایه بازشناسی چهره و موقعیت مکانی GPS',
        'domain': 'biometrics_vision',
        'abstract_en': 'A tamper-proof mobile biometric clocking platform utilizing lightweight CNN face verification and geo-fenced coordinates.',
        'abstract_fa': 'سامانه امن حضور و غیاب بر روی گوشی‌های هوشمند با تایید بیومتریک چهره و حصارکشی جغرافیایی ماهواره‌ای.'
    },
    {
        'id': 'th_2017_2',
        'year': 2017,
        'degree': 'M.Sc.',
        'student_en': 'Fozie Gholamrezai',
        'student_fa': 'فوزیه غلامرضایی',
        'title_en': 'Biometric Identification Based on Dorsal Hand Vein Pattern Recognition',
        'title_fa': 'احراز هویت بیومتریک مبتنی بر بازشناسی الگوی ورید پشت دست',
        'domain': 'biometrics_vision',
        'abstract_en': 'Near-infrared dorsal venous vascular mapping offering spoof-proof personal identity verification.',
        'abstract_fa': 'تصویربرداری مادون قرمز نزدیک از ساختار عروقی ورید پشت دست جهت احراز هویت غیرقابل جعل.'
    },
    {
        'id': 'th_2016_2',
        'year': 2016,
        'degree': 'M.Sc.',
        'student_en': 'Hawraa Almulimawi',
        'student_fa': 'حوراء المعلموای',
        'title_en': 'Bone Fracture Image Texture Recognition and Computer-Aided Classification',
        'title_fa': 'تشخیص و رده‌بندی بافت شکستگی‌های استخوان در تصاویر رادیولوژی',
        'domain': 'medical_imaging',
        'abstract_en': 'Automated orthopedic diagnosis detecting hairline bone fissures on X-ray radiography using directional texture gradients.',
        'abstract_fa': 'تشخیص رایانه‌ای شکستگی‌ها و ترک‌های مویی استخوان در رادیوگرافی‌های بالینی با گرادیان‌های بافت.'
    },
    {
        'id': 'th_2013_1',
        'year': 2013,
        'degree': 'M.Sc.',
        'student_en': 'Bahare Jalilian',
        'student_fa': 'بهاره جلیلیان',
        'title_en': 'Persian Sign Language Recognition Using Hand Contour Radial Distance Vectors',
        'title_fa': 'بازشناسی زبان اشاره فارسی با استفاده از بردارهای فاصله شعاعی کانتور دست',
        'domain': 'biometrics_vision',
        'abstract_en': 'Static and dynamic gesture decoding system translating Iranian sign language letters into spoken text.',
        'abstract_fa': 'سیستم ترجمه حرکات دست به حروف و واژگان فارسی جهت تسهیل ارتباط ناشنوایان با جامعه.'
    }
])

# Chart data: Publications distribution over time and across research fields
analytics = {
    "yearly_trends": [
        {"year": 2002, "count": 2},
        {"year": 2003, "count": 4},
        {"year": 2004, "count": 8},
        {"year": 2005, "count": 5},
        {"year": 2006, "count": 3},
        {"year": 2007, "count": 4},
        {"year": 2008, "count": 4},
        {"year": 2009, "count": 3},
        {"year": 2010, "count": 5},
        {"year": 2011, "count": 6},
        {"year": 2012, "count": 4},
        {"year": 2013, "count": 7},
        {"year": 2014, "count": 6},
        {"year": 2015, "count": 3},
        {"year": 2016, "count": 6},
        {"year": 2017, "count": 4},
        {"year": 2018, "count": 5},
        {"year": 2019, "count": 4},
        {"year": 2020, "count": 5},
        {"year": 2021, "count": 7},
        {"year": 2022, "count": 10},
        {"year": 2023, "count": 8},
        {"year": 2024, "count": 6},
        {"year": 2025, "count": 4},
        {"year": 2026, "count": 5}
    ],
    "citations_trajectory": [
        {"year": 2005, "annual": 15, "cumulative": 15},
        {"year": 2007, "annual": 28, "cumulative": 58},
        {"year": 2009, "annual": 35, "cumulative": 128},
        {"year": 2011, "annual": 48, "cumulative": 218},
        {"year": 2013, "annual": 62, "cumulative": 340},
        {"year": 2015, "annual": 75, "cumulative": 485},
        {"year": 2017, "annual": 82, "cumulative": 651},
        {"year": 2019, "annual": 98, "cumulative": 845},
        {"year": 2021, "annual": 125, "cumulative": 1080},
        {"year": 2023, "annual": 152, "cumulative": 1280},
        {"year": 2024, "annual": 165, "cumulative": 1345},
        {"year": 2025, "annual": 175, "cumulative": 1390},
        {"year": 2026, "annual": 185, "cumulative": 1412}
    ],
    "domain_distribution": [
        {"domain": "medical_imaging", "label_en": "Medical AI & Healthcare Imaging", "label_fa": "هوش مصنوعی پزشکی و تصاویر بالینی", "percentage": 30, "count": 33, "color": "#06B6D4"},
        {"domain": "ai_deeplearning", "label_en": "Deep Learning & Vision Architectures", "label_fa": "معماری‌های یادگیری عمیق و بینایی", "percentage": 25, "count": 28, "color": "#6366F1"},
        {"domain": "biometrics_vision", "label_en": "Biometrics & Pattern Recognition", "label_fa": "بیومتریک و بازشناسی الگو", "percentage": 20, "count": 22, "color": "#10B981"},
        {"domain": "distributed_fog", "label_en": "Distributed Systems & Fog/Cloud", "label_fa": "سیستم‌های توزیع‌شده و محاسبات مه", "percentage": 15, "count": 17, "color": "#F59E0B"},
        {"domain": "nlp_sentiment", "label_en": "NLP & Language Modeling", "label_fa": "پردازش زبان طبیعی و مدل‌سازی متن", "percentage": 10, "count": 11, "color": "#EC4899"}
    ],
    "venue_breakdown": [
        {"id": "q1_journals", "label_en": "Q1 Flagship Journals (IEEE, Elsevier, Springer)", "label_fa": "نشریات برتر رده Q1 بین‌المللی", "percentage": 40, "count": 44, "color": "#6366F1"},
        {"id": "conferences", "label_en": "International Flagship Conferences (IEEE ICIP, ICME)", "label_fa": "همایش‌های معتبر بین‌المللی (IEEE)", "percentage": 35, "count": 39, "color": "#06B6D4"},
        {"id": "indexed", "label_en": "Indexed Journals & Book Chapters (LNCS, etc.)", "label_fa": "مجلات نمایه‌شده و فصول کتب علمی", "percentage": 20, "count": 22, "color": "#10B981"},
        {"id": "patents", "label_en": "Patents & Commercial Technology", "label_fa": "ثبت اختراعات و فناوری‌های صنعتی", "percentage": 5, "count": 5, "color": "#F59E0B"}
    ],
    "radar_competencies": [
        {"axis_en": "Computer Vision & DIP", "axis_fa": "بینایی ماشین و پردازش تصویر", "score": 95},
        {"axis_en": "Medical AI & Healthcare CAD", "axis_fa": "هوش مصنوعی و پردازش پزشکی", "score": 92},
        {"axis_en": "Deep Learning Architectures", "axis_fa": "معماری‌های یادگیری عمیق", "score": 90},
        {"axis_en": "Meta-heuristic Optimization", "axis_fa": "الگوریتم‌های فراابتکاری", "score": 88},
        {"axis_en": "Distributed & Fog Systems", "axis_fa": "سیستم‌های توزیع‌شده و مه", "score": 85},
        {"axis_en": "Natural Language Processing", "axis_fa": "پردازش زبان طبیعی (NLP)", "score": 82}
    ],
    "theses_evolution": [
        {"era": "2024–2026", "theses_count": 16, "primary_focus_en": "3D Medical CT, Ultrasound, IoMT Federated Learning", "primary_focus_fa": "سی‌تی ۳بعدی پزشکی، سونوگرافی، یادگیری فدرال"},
        {"era": "2020–2023", "theses_count": 28, "primary_focus_en": "Deep Biometrics, NLP Sentiment, Brain MRI Glioblastoma", "primary_focus_fa": "بیومتریک عمیق، پردازش متن، ام‌آر‌آی مغز"},
        {"era": "2016–2019", "theses_count": 22, "primary_focus_en": "Orthopedic Radiography, Art Stylometry, Mobile Biometrics", "primary_focus_fa": "رادیولوژی استخوان، سبک‌سنجی نقاشی، بیومتریک موبایل"},
        {"era": "2012–2015", "theses_count": 19, "primary_focus_en": "CUDA Parallel Acceleration, Sign Language, Cloud Schedulers", "primary_focus_fa": "شتاب‌بخشی موازی CUDA، زبان اشاره، زمان‌بندی ابری"}
    ],
    "global_collaborations": [
        {"region_en": "Australia (Univ. of Wollongong)", "region_fa": "استرالیا (دانشگاه ولونگونگ)", "papers": 14, "flag": "🇦🇺"},
        {"region_en": "Germany (Univ. of Luebeck / Rostock)", "region_fa": "آلمان (دانشگاه لوبک و روستوک)", "papers": 8, "flag": "🇩🇪"},
        {"region_en": "Iran (Sharif Univ. & Razi Univ.)", "region_fa": "ایران (دانشگاه شریف و دانشگاه رازی)", "papers": 75, "flag": "🇮🇷"},
        {"region_en": "Middle East & International", "region_fa": "همکاری‌های منطقه‌ای و بین‌المللی", "papers": 13, "flag": "🌐"}
    ]
}

data_export = {
    "profile": profile,
    "research_interests": research_interests,
    "education": education,
    "leadership": leadership,
    "courses": courses,
    "patents": patents,
    "applied_projects": applied_projects,
    "publications": publications,
    "theses": theses,
    "analytics": analytics
}

js_content = f"// Comprehensive Bilingual Academic Dataset for Dr. Abdolah Chalechale\nwindow.ACADEMIC_DATA = {json.dumps(data_export, ensure_ascii=False, indent=2)};\n"

with open("assets/js/data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated assets/js/data.js successfully! (Total bytes: {len(js_content)})")
