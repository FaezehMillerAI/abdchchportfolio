/**
 * Dr. Abdolah Chalechale - Multi-Page Academic Portfolio & Interactive CV
 * Shared Controller & Advanced Dynamic Analytics Visualization Engine
 */

(function () {
  'use strict';

  // --- UI Translation Dictionary ---
  const UI_TEXT = {
    en: {
      site_title: "Dr. Abdolah Chalechale | Academic Portfolio & CV",
      nav_home: "Home",
      nav_publications: "Publications",
      nav_theses: "Theses",
      nav_experience: "Experience",
      nav_teaching: "Teaching",
      nav_projects: "Patents & Projects",
      nav_contact: "Contact",
      brand_sub: "Razi University",
      print_cv: "CV (PDF)",
      verified_prof: "Verified Faculty Member",
      citations_label: "Total Citations",
      hindex_label: "h-index",
      i10index_label: "i10-index",
      pubs_label: "Publications & Patents",
      theses_label: "Supervised Theses",
      exp_label: "Years in Academia",
      recent_sub: "Google Scholar Verified",
      
      // Home Page
      home_pillars_tag: "Core Research Pillars",
      home_pillars_title: "Research Specializations & Frontiers",
      home_pillars_desc: "Pioneering investigations across Deep Learning, Medical Imaging, NLP, and Distributed Computing.",
      home_featured_tag: "Recent Breakthroughs",
      home_featured_title: "Selected High-Impact Publications (2024–2026)",
      home_featured_desc: "Cutting-edge contributions published in Q1 flagship journals including Applied Soft Computing, AI Review, and Cluster Computing.",
      explore_all_pubs: "Explore All Publications →",
      explore_all_theses: "View Supervised Theses →",
      
      // Publications Page
      pubs_page_title: "Publications & Research Hub",
      pubs_page_subtitle: "Comprehensive archive of peer-reviewed journal papers, international conference articles, and patents.",
      search_placeholder: "Search by title, author, venue, or keyword (e.g. 'DenseNet', 'Federated', 'Biometric')...",
      filter_all: "All Works",
      filter_journals: "Journal Articles",
      filter_conferences: "Conferences",
      filter_highlights: "Selected Highlights",
      filter_all_topics: "All Research Topics",
      sort_newest: "Sort: Newest First",
      sort_oldest: "Sort: Oldest First",
      sort_title: "Sort: By Title",
      copy_bibtex: "Copy BibTeX",
      copy_apa: "Copy APA",
      view_abstract: "Abstract & Details",

      // Chart Tabs & Analytics
      chart_tab_pubs: "📊 Publications Momentum",
      chart_tab_citations: "📈 Citations Growth",
      chart_tab_venues: "🍩 Venue & Publisher Breakdown",
      chart_tab_radar: "🕸️ Research Competency Radar",
      chart_tab_collab: "🌐 International Collaboration",
      
      // Theses Page
      theses_page_title: "Supervised Graduate Theses",
      theses_page_subtitle: "Mentoring postgraduate researchers in deep learning, medical diagnosis, speech processing, and smart systems.",
      theses_search_placeholder: "Search student name, thesis topic, or dataset (e.g. 'Pancreas', 'Safari', 'Liver')...",
      filter_all_years: "All Years",
      researcher_label: "Student:",
      
      // Experience Page
      exp_page_title: "Academic Background & Leadership",
      exp_page_subtitle: "Graduated from Sharif University and University of Wollongong; over three decades of department and computing center leadership.",
      
      // Teaching Page
      teaching_page_title: "Teaching & Academic Instruction",
      teaching_page_subtitle: "Undergraduate and graduate curricula in computer systems, artificial intelligence, and software engineering.",
      units_text: "Units",
      
      // Projects Page
      projects_page_title: "Patents & Applied Research Grants",
      projects_page_subtitle: "Registered national inventions, industrial contracts, and commercialized hardware-software solutions.",
      
      // Contact Page
      contact_page_title: "Office & Contact Information",
      contact_page_subtitle: "Direct channels for academic inquiries, prospective graduate students, and scientific collaboration.",
      office_title: "Department Office",
      email_title: "Direct Emails",
      phone_title: "Office Phone",
      profiles_title: "Academic Portals",
      
      // Messages & Notifications
      bibtex_copied: "BibTeX citation copied to clipboard!",
      apa_copied: "APA citation copied to clipboard!",
      no_results: "No records found matching your query. Please try different filters or keywords.",
      modal_close: "Close",
      all_rights: "All rights reserved. Official Academic Portfolio of Dr. Abdolah Chalechale."
    },
    fa: {
      site_title: "دکتر عبدالله چاله چاله | پورتفولیو و رزومه علمی",
      nav_home: "صفحه اصلی",
      nav_publications: "مقالات",
      nav_theses: "پایان‌نامه‌ها",
      nav_experience: "سوابق علمی",
      nav_teaching: "دروس",
      nav_projects: "اختراعات",
      nav_contact: "تماس",
      brand_sub: "دانشگاه رازی",
      print_cv: "رزومه PDF",
      verified_prof: "عضو رسمی هیئت علمی",
      citations_label: "استنادات کل (Citations)",
      hindex_label: "شاخص اچ (h-index)",
      i10index_label: "شاخص i10-index",
      pubs_label: "مقالات و اختراعات",
      theses_label: "پایان‌نامه‌های هدایت‌شده",
      exp_label: "سال سابقه علمی و دانشگاهی",
      recent_sub: "مستند در گوگل اسکولار",
      
      // Home Page
      home_pillars_tag: "محورهای تخصصی",
      home_pillars_title: "حوزه‌های اصلی پژوهش و مرزهای دانش",
      home_pillars_desc: "پژوهش‌های بنیادین و کاربردی در یادگیری عمیق، پردازش تصاویر پزشکی، پردازش زبان طبیعی و سیستم‌های توزیع‌شده.",
      home_featured_tag: "دستاوردهای اخیر",
      home_featured_title: "مقالات برگزیده سال‌های ۲۰۲۴ تا ۲۰۲۶",
      home_featured_desc: "دستاوردهای منتشرشده در نشریات برتر رده Q1 از جمله Applied Soft Computing، AI Review و Cluster Computing.",
      explore_all_pubs: "مشاهده تمام مقالات و پژوهش‌ها ←",
      explore_all_theses: "مشاهده آرشیو پایان‌نامه‌ها ←",
      
      // Publications Page
      pubs_page_title: "مرکز مقالات و پژوهش‌های علمی",
      pubs_page_subtitle: "آرشیو جامع بیش از ۱۰۰ مقاله داوری‌شده در مجلات معتبر بین‌المللی، کنفرانس‌های معتبر و فصول کتب علمی.",
      search_placeholder: "جستجو در عنوان، نام نویسنده، مجله یا سال انتشار (مثلاً: 'پانکراس', 'فدرال', 'DenseNet')...",
      filter_all: "همه مقالات",
      filter_journals: "مجلات علمی",
      filter_conferences: "کنفرانس‌ها",
      filter_highlights: "مقالات برگزیده",
      filter_all_topics: "همه حوزه‌های پژوهشی",
      sort_newest: "مرتب‌سازی: جدیدترین",
      sort_oldest: "مرتب‌سازی: قدیمی‌ترین",
      sort_title: "مرتب‌سازی: الفبایی",
      copy_bibtex: "کپی BibTeX",
      copy_apa: "کپی ارجاع APA",
      view_abstract: "چکیده و جزئیات",

      // Chart Tabs & Analytics
      chart_tab_pubs: "📊 روند زمانی مقالات",
      chart_tab_citations: "📈 رشد استنادات (Citations)",
      chart_tab_venues: "🍩 توزیع نشریات و مقالات",
      chart_tab_radar: "🕸️ رادار شایستگی‌های علمی",
      chart_tab_collab: "🌐 همکاری‌های بین‌المللی",
      
      // Theses Page
      theses_page_title: "پایان‌نامه‌ها و دانش‌آموختگان",
      theses_page_subtitle: "راهنمایی و هدایت پژوهشگران کارشناسی ارشد و دکتری در هوش مصنوعی، تصویربرداری پزشکی و سیستم‌های توزیع‌شده.",
      theses_search_placeholder: "جستجو در نام دانشجو، عنوان پایان‌نامه یا موضوع (مثلاً: 'صفری', 'پانکراس', 'کبد')...",
      filter_all_years: "همه سال‌ها",
      researcher_label: "دانشجو:",
      
      // Experience Page
      exp_page_title: "سوابق تحصیلی و مسئولیت‌های اجرایی",
      exp_page_subtitle: "فارغ‌التحصیل دانشگاه صنعتی شریف و دانشگاه ولونگونگ استرالیا؛ بیش از سه دهه خدمت در مدیریت گروه و مرکز محاسبات دانشگاه رازی.",
      
      // Teaching Page
      teaching_page_title: "دروس و سرفصل‌های تدریس‌شده",
      teaching_page_subtitle: "تدریس دروس تخصصی مقاطع تحصیلات تکمیلی و کارشناسی در رشته مهندسی کامپیوتر و هوش مصنوعی.",
      units_text: "واحد",
      
      // Projects Page
      projects_page_title: "ثبت اختراع و طرح‌های کاربردی",
      projects_page_subtitle: "اختراعات ثبت‌شده رسمی، قراردادهای ارتباط با صنعت و فناوری‌های کاربردی توسعه‌یافته.",
      
      // Contact Page
      contact_page_title: "اطلاعات تماس و دفتر کار",
      contact_page_subtitle: "راه‌های ارتباط مستقیم جهت هماهنگی جلسات علمی، راهنمایی پایان‌نامه و همکاری‌های پژوهشی.",
      office_title: "دفتر کار اصلی",
      email_title: "پست الکترونیک",
      phone_title: "تلفن مستقیم",
      profiles_title: "صفحات دانشگاهی",
      
      // Messages & Notifications
      bibtex_copied: "ارجاع BibTeX در حافظه کپی شد!",
      apa_copied: "ارجاع APA در حافظه کپی شد!",
      no_results: "موردی مطابق با جستجوی شما یافت نشد. لطفاً عبارت یا فیلتر دیگری را امتحان کنید.",
      modal_close: "بستن",
      all_rights: "تمامی حقوق محفوظ است. وب‌سایت و پورتفولیوی رسمی دکتر عبدالله چاله چاله."
    }
  };

  // --- Application State ---
  const state = {
    lang: localStorage.getItem('chalechale_lang') || 'fa',
    theme: localStorage.getItem('chalechale_theme') || 'dark',
    activeChartTab: 'publications', // 'publications' | 'citations' | 'venues' | 'radar' | 'collaborations'
    pubCategory: 'all',
    pubTopic: 'all',
    pubSearch: '',
    pubSort: 'newest',
    thesisYear: 'all',
    thesisSearch: '',
    mobileMenuOpen: false
  };

  // --- Helper: Get translation ---
  function t(key) {
    const dict = UI_TEXT[state.lang] || UI_TEXT.en;
    return dict[key] || key;
  }

  // --- Helper: Format APA Citation ---
  function formatAPA(pub) {
    const authors = pub.authors || "Chalechale, A.";
    const year = pub.year || "2024";
    const title = pub.title_en || pub.title_fa || "";
    const venue = pub.journal_en || pub.conference_en || "";
    const pages = pub.pages ? `, pp. ${pub.pages}` : "";
    return `${authors} (${year}). ${title}. ${venue}${pages}.`;
  }

  // --- Helper: Format BibTeX Citation ---
  function formatBibTeX(pub) {
    const key = `chalechale${pub.year}_${(pub.id || 'pub').replace(/[^a-zA-Z0-9]/g, '')}`;
    const type = pub.category === 'journal' ? 'article' : 'inproceedings';
    let bib = `@${type}{${key},\n`;
    bib += `  author = {${pub.authors}},\n`;
    bib += `  title = {{${pub.title_en}}},\n`;
    if (pub.category === 'journal') {
      bib += `  journal = {${pub.journal_en}},\n`;
    } else {
      bib += `  booktitle = {${pub.conference_en}},\n`;
    }
    bib += `  year = {${pub.year}}`;
    if (pub.pages) bib += `,\n  pages = {${pub.pages}}`;
    if (pub.publisher) bib += `,\n  publisher = {${pub.publisher}}`;
    if (pub.doi) bib += `,\n  doi = {${pub.doi}}`;
    bib += `\n}`;
    return bib;
  }

  // --- Toast Notification ---
  function showToast(msg) {
    const shelf = document.getElementById('toast-shelf');
    if (!shelf) return;
    const bubble = document.createElement('div');
    bubble.className = 'toast-bubble';
    bubble.innerHTML = `<span style="color:#10b981; font-weight:bold;">✓</span> <span>${msg}</span>`;
    shelf.appendChild(bubble);
    setTimeout(() => {
      bubble.style.opacity = '0';
      bubble.style.transform = 'translateY(15px) scale(0.95)';
      bubble.style.transition = 'all 0.3s ease';
      setTimeout(() => bubble.remove(), 300);
    }, 2600);
  }

  // --- Identify Current Page ---
  function getCurrentPageName() {
    const path = window.location.pathname;
    const page = path.split('/').pop() || 'index.html';
    if (page === '' || page === 'index.html') return 'home';
    if (page.includes('publication')) return 'publications';
    if (page.includes('theses') || page.includes('thesis')) return 'theses';
    if (page.includes('experience') || page.includes('timeline')) return 'experience';
    if (page.includes('teaching') || page.includes('course')) return 'teaching';
    if (page.includes('project') || page.includes('patent')) return 'projects';
    if (page.includes('contact')) return 'contact';
    return 'home';
  }

  // --- Render Header ---
  function renderHeader() {
    const headerEl = document.getElementById('app-header');
    if (!headerEl) return;

    const currentPage = getCurrentPageName();
    const isFa = state.lang === 'fa';
    const profile = window.ACADEMIC_DATA.profile;

    const navItems = [
      { id: 'home', url: 'index.html', label_en: 'Home', label_fa: 'صفحه اصلی' },
      { id: 'publications', url: 'publications.html', label_en: 'Publications', label_fa: 'مقالات' },
      { id: 'theses', url: 'theses.html', label_en: 'Theses', label_fa: 'پایان‌نامه‌ها' },
      { id: 'experience', url: 'experience.html', label_en: 'Experience', label_fa: 'سوابق علمی' },
      { id: 'teaching', url: 'teaching.html', label_en: 'Teaching', label_fa: 'دروس' },
      { id: 'projects', url: 'projects.html', label_en: 'Patents', label_fa: 'اختراعات' },
      { id: 'contact', url: 'contact.html', label_en: 'Contact', label_fa: 'تماس' }
    ];

    const linksHtml = navItems.map(item => `
      <li class="nav-item">
        <a href="${item.url}" class="nav-link ${currentPage === item.id ? 'active' : ''}">
          ${isFa ? item.label_fa : item.label_en}
        </a>
      </li>
    `).join('');

    const mobileLinksHtml = navItems.map(item => `
      <a href="${item.url}" class="mobile-nav-link ${currentPage === item.id ? 'active' : ''}">
        ${isFa ? item.label_fa : item.label_en}
      </a>
    `).join('');

    headerEl.innerHTML = `
      <nav class="navbar">
        <div class="container nav-container">
          <!-- Brand -->
          <a href="index.html" class="nav-brand">
            <img src="assets/images/profile.jpg" alt="${isFa ? profile.name.fa : profile.name.en}" class="brand-avatar">
            <div class="brand-info">
              <span class="brand-name">${isFa ? profile.name.fa : profile.name.en}</span>
              <span class="brand-badge">${t('brand_sub')}</span>
            </div>
          </a>

          <!-- Desktop Navigation -->
          <div class="nav-menu-wrapper">
            <ul class="nav-menu">
              ${linksHtml}
            </ul>
          </div>

          <!-- Actions -->
          <div class="nav-actions">
            <button class="action-pill" onclick="window.toggleLanguage()" title="${isFa ? 'Switch to English' : 'تغییر به فارسی'}">
              <span>🌐</span>
              <span>${isFa ? 'English' : 'فارسی'}</span>
            </button>

            <button class="icon-btn-round" onclick="window.toggleTheme()" title="${state.theme === 'dark' ? 'Switch to Light Mode' : 'حالت شب'}">
              ${state.theme === 'dark'
                ? `<svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>`
                : `<svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>`
              }
            </button>

            <button class="action-pill primary" onclick="window.print()" title="Print CV / Save as PDF">
              <svg width="15" height="15" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/>
              </svg>
              <span>${t('print_cv')}</span>
            </button>

            <button class="mobile-toggle" onclick="window.toggleMobileMenu()" aria-label="Toggle Navigation">
              <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/>
              </svg>
            </button>
          </div>
        </div>
      </nav>

      <div id="mobile-drawer" class="mobile-nav-drawer ${state.mobileMenuOpen ? 'active' : ''}">
        ${mobileLinksHtml}
      </div>
    `;
  }

  // --- Render Footer ---
  function renderFooter() {
    const footerEl = document.getElementById('app-footer');
    if (!footerEl) return;

    footerEl.innerHTML = `
      <footer class="footer">
        <div class="container footer-inner">
          <div class="footer-copy">
            <span>${t('all_rights')}</span>
            <div style="font-size:0.75rem; color:var(--text-faint); margin-top:3px;">
              Designed with precision · Deployable on GitHub Pages
            </div>
          </div>
          <div class="footer-nav">
            <a href="https://scholar.google.com/citations?user=C1-FBkUAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
            <a href="https://en.razi.ac.ir/~chalechale/home" target="_blank" rel="noopener">Razi University Portal</a>
            <a href="contact.html">${state.lang === 'fa' ? 'تماس با استاد' : 'Contact'}</a>
          </div>
        </div>
      </footer>
      <div id="toast-shelf" class="toast-shelf"></div>
    `;
  }

  // --- Render Subpage Header Banner ---
  function renderSubpageBanner(titleKey, subtitleKey, breadcrumbLabel) {
    const bannerEl = document.getElementById('subpage-banner');
    if (!bannerEl) return;
    const isFa = state.lang === 'fa';

    bannerEl.innerHTML = `
      <section class="page-header-section">
        <div class="container page-header-content">
          <div class="page-breadcrumb">
            <a href="index.html">${t('nav_home')}</a>
            <span>${isFa ? '←' : '→'}</span>
            <span>${breadcrumbLabel}</span>
          </div>
          <h1 class="page-title">${t(titleKey)}</h1>
          <p class="page-subtitle">${t(subtitleKey)}</p>
        </div>
      </section>
    `;
  }

  // =========================================================================
  // ADVANCED INTERACTIVE CHART ENGINE (5 High-End Chart Visualizations)
  // =========================================================================

  function renderInteractiveChartSuite() {
    const container = document.getElementById('analytics-suite-container');
    if (!container) return;

    const isFa = state.lang === 'fa';
    const analytics = window.ACADEMIC_DATA.analytics;

    // Tabs definition
    const chartTabs = [
      { id: 'publications', icon: '📊', label_en: 'Publications Momentum', label_fa: 'روند مقالات' },
      { id: 'citations', icon: '📈', label_en: 'Citations Growth (1,400+)', label_fa: 'رشد استنادات (۱۴۰۰+)' },
      { id: 'venues', icon: '🍩', label_en: 'Venue & Publisher Breakdown', label_fa: 'توزیع نشریات و همایش‌ها' },
      { id: 'radar', icon: '🕸️', label_en: 'Research Competency Radar', label_fa: 'رادار شایستگی‌های علمی' },
      { id: 'collaborations', icon: '🌐', label_en: 'Global Network', label_fa: 'همکاری‌های بین‌المللی' }
    ];

    const tabsHtml = chartTabs.map(tab => `
      <button class="chart-tab-pill ${state.activeChartTab === tab.id ? 'active' : ''}" onclick="window.switchChartTab('${tab.id}')">
        <span>${tab.icon}</span>
        <span>${isFa ? tab.label_fa : tab.label_en}</span>
      </button>
    `).join('');

    let chartSvgHtml = '';
    let sidebarMetricsHtml = '';

    // 1. Publications Momentum Bar Chart & Domain Breakdown
    if (state.activeChartTab === 'publications') {
      const yearly = analytics.yearly_trends;
      const width = 640;
      const height = 240;
      const padLeft = 32;
      const padBottom = 32;
      const padTop = 20;
      const padRight = 15;
      const maxCount = Math.max(...yearly.map(d => d.count), 10);
      const barWidth = Math.floor((width - padLeft - padRight) / yearly.length) - 4;

      let bars = '';
      yearly.forEach((d, i) => {
        const x = padLeft + i * (barWidth + 4);
        const barH = ((height - padBottom - padTop) * d.count) / maxCount;
        const y = height - padBottom - barH;
        const tipMsg = `${d.year}: ${d.count} ` + (isFa ? 'مقاله (کلیک برای فیلتر)' : 'papers (click to filter)');
        bars += `
          <g class="chart-bar-group" onclick="window.filterByYear(${d.year})" style="cursor:pointer;">
            <rect x="${x}" y="${y}" width="${barWidth}" height="${barH}" rx="3" fill="var(--primary)" opacity="0.85"
                  data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
            </rect>
            ${(i % 3 === 0 || i === yearly.length - 1) ? `
              <text x="${x + barWidth / 2}" y="${height - 10}" text-anchor="middle" font-size="9" fill="var(--text-faint)" font-family="inherit">${d.year}</text>
            ` : ''}
            <text x="${x + barWidth / 2}" y="${y - 5}" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--text-main)">${d.count}</text>
          </g>
        `;
      });

      chartSvgHtml = `
        <div style="width:100%;">
          <div style="font-size:1.05rem; font-weight:800; margin-bottom:1rem; text-align:center; color:var(--text-main);">
            📈 ${isFa ? 'روند سالانه انتشارات علمی (۲۰۰۲ – ۲۰۲۶)' : 'Annual Scientific Publication Trends (2002 – 2026)'}
          </div>
          <svg viewBox="0 0 ${width} ${height}" style="width:100%; height:auto; overflow:visible;">
            <line x1="${padLeft}" y1="${height - padBottom}" x2="${width - padRight}" y2="${height - padBottom}" stroke="var(--border-color)" stroke-width="1"/>
            ${bars}
          </svg>
        </div>
      `;

      // Domain Breakdown sidebar with clickable bars matching user screenshot
      const domains = analytics.domain_distribution;
      const domainBarsHtml = domains.map(dm => `
        <div class="domain-bar-item" onclick="window.filterByTopic('${dm.key}')" title="${isFa ? 'کلیک برای فیلتر مقالات این حوزه' : 'Click to filter papers in this domain'}">
          <div class="domain-bar-header">
            <span style="display:flex; align-items:center; gap:0.4rem;">
              <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:${dm.color};"></span>
              <span>${isFa ? dm.name_fa : dm.name_en}</span>
            </span>
            <span style="color:${dm.color}; font-weight:800;">${dm.percentage}%</span>
          </div>
          <div class="domain-bar-track">
            <div class="domain-bar-fill" style="width:${dm.percentage}%; background:${dm.color};"></div>
          </div>
        </div>
      `).join('');

      sidebarMetricsHtml = `
        <div>
          <div style="font-size:1rem; font-weight:800; margin-bottom:0.9rem; display:flex; align-items:center; gap:0.45rem; color:var(--text-main);">
            <span>🎯</span>
            <span>${isFa ? 'سهم حوزه‌های تخصصی' : 'Research Domains Breakdown'}</span>
          </div>
          <div class="domain-interactive-list">
            ${domainBarsHtml}
          </div>
          <div style="margin-top:1.1rem; padding-top:0.9rem; border-top:1px solid var(--border-color); font-size:0.76rem; color:var(--text-faint); text-align:center;">
            ${isFa ? '💡 نکته: با کلیک روی هر حوزه یا ستون سال، مقالات فیلتر می‌شوند.' : '💡 Tip: Click any domain or year column to filter publications.'}
          </div>
        </div>
      `;
    }

    // 2. Citations Growth Curve (Area / Spline SVG)
    else if (state.activeChartTab === 'citations') {
      const data = analytics.citations_trajectory;
      const width = 640;
      const height = 240;
      const padLeft = 45;
      const padBottom = 32;
      const padTop = 20;
      const padRight = 20;
      const maxC = 1500;
      const stepX = (width - padLeft - padRight) / (data.length - 1);

      let polyPoints = [`${padLeft},${height - padBottom}`];
      let linePoints = [];
      let dots = '';

      data.forEach((d, i) => {
        const x = padLeft + i * stepX;
        const y = height - padBottom - ((d.cumulative / maxC) * (height - padBottom - padTop));
        polyPoints.push(`${x},${y}`);
        linePoints.push(`${x},${y}`);
        const tipMsg = `${d.year}: ${d.cumulative.toLocaleString()} ` + (isFa ? `استناد کل (رشد سالانه: +${d.annual})` : `citations (+${d.annual})`);
        dots += `
          <circle cx="${x}" cy="${y}" class="area-point"
                  data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
          </circle>
          ${(i % 2 === 0 || i === data.length - 1) ? `
            <text x="${x}" y="${height - 10}" text-anchor="middle" font-size="9" fill="var(--text-faint)">${d.year}</text>
          ` : ''}
        `;
      });
      polyPoints.push(`${padLeft + (data.length - 1) * stepX},${height - padBottom}`);

      chartSvgHtml = `
        <svg viewBox="0 0 ${width} ${height}" style="width:100%; height:auto; overflow:visible;">
          <defs>
            <linearGradient id="citGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="var(--cyan)" stop-opacity="0.45"/>
              <stop offset="100%" stop-color="var(--cyan)" stop-opacity="0.0"/>
            </linearGradient>
          </defs>
          <line x1="${padLeft}" y1="${height - padBottom}" x2="${width - padRight}" y2="${height - padBottom}" stroke="var(--border-color)" stroke-width="1"/>
          <!-- Grid lines -->
          <line x1="${padLeft}" y1="${height - padBottom - (height - padBottom - padTop) * 0.5}" x2="${width - padRight}" y2="${height - padBottom - (height - padBottom - padTop) * 0.5}" stroke="var(--border-color)" stroke-dasharray="4" stroke-width="1"/>
          <text x="${padLeft - 6}" y="${height - padBottom - (height - padBottom - padTop) * 0.5 + 4}" text-anchor="end" font-size="8" fill="var(--text-faint)">750</text>
          <text x="${padLeft - 6}" y="${padTop + 8}" text-anchor="end" font-size="8" fill="var(--text-faint)">1,500</text>

          <polygon points="${polyPoints.join(' ')}" fill="url(#citGrad)"/>
          <polyline points="${linePoints.join(' ')}" class="area-line"/>
          ${dots}
        </svg>
      `;

      sidebarMetricsHtml = `
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'استنادات کل (Google Scholar):' : 'Total Citations:'}</span>
          <span class="metric-value" style="color:var(--cyan);">1,412+</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'شاخص اچ (h-index):' : 'h-index:'}</span>
          <span class="metric-value">18</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'شاخص i10-index:' : 'i10-index:'}</span>
          <span class="metric-value">31</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'استنادات از سال ۲۰۱۹ تاکنون:' : 'Citations Since 2019:'}</span>
          <span class="metric-value" style="color:var(--emerald);">761 (54%)</span>
        </div>
        <div style="font-size:0.75rem; color:var(--text-faint); margin-top:0.5rem; text-align:center;">
          ${isFa ? 'رشد تصاعدی استنادات نشان‌دهنده ضریب نفوذ و ارجاع بالای مقالات در هوش مصنوعی مدرن است.' : 'Accelerating citation curve highlights high impact across foundational AI literature.'}
        </div>
      `;
    }

    // 3. Venue Breakdown Donut Chart
    else if (state.activeChartTab === 'venues') {
      const venues = analytics.venue_breakdown;
      const cx = 150;
      const cy = 140;
      const R = 105;
      const r = 62;
      let startDeg = 0;
      let slicesSvg = '';

      venues.forEach(vn => {
        const span = (vn.percentage / 100.0) * 360;
        const endDeg = startDeg + span;
        const a1 = (startDeg - 90) * (Math.PI / 180);
        const a2 = (endDeg - 90) * (Math.PI / 180);
        const x1 = cx + R * Math.cos(a1);
        const y1 = cy + R * Math.sin(a1);
        const x2 = cx + R * Math.cos(a2);
        const y2 = cy + R * Math.sin(a2);
        const ix1 = cx + r * Math.cos(a1);
        const iy1 = cy + r * Math.sin(a1);
        const ix2 = cx + r * Math.cos(a2);
        const iy2 = cy + r * Math.sin(a2);
        const largeArc = span > 180 ? 1 : 0;
        const d = `M ${x1} ${y1} A ${R} ${R} 0 ${largeArc} 1 ${x2} ${y2} L ${ix2} ${iy2} A ${r} ${r} 0 ${largeArc} 0 ${ix1} ${iy1} Z`;

        const vnLabel = isFa ? vn.label_fa : vn.label_en;
        const tipMsg = `${vnLabel}: ${vn.count} (${vn.percentage}%)`;
        slicesSvg += `
          <path d="${d}" fill="${vn.color}" class="donut-slice"
                data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
          </path>
        `;
        startDeg = endDeg;
      });

      chartSvgHtml = `
        <svg viewBox="0 0 300 280" style="width:100%; max-width:320px; height:auto; overflow:visible;">
          ${slicesSvg}
          <circle cx="${cx}" cy="${cy}" r="${r - 2}" fill="var(--bg-surface)"/>
          <text x="${cx}" y="${cy - 6}" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--text-main)">110+</text>
          <text x="${cx}" y="${cy + 14}" text-anchor="middle" font-size="9" fill="var(--text-faint)">${isFa ? 'مجموع آثار' : 'Total Works'}</text>
        </svg>
      `;

      sidebarMetricsHtml = venues.map(vn => `
        <div style="display:flex; flex-direction:column; gap:0.25rem;">
          <div style="display:flex; justify-content:space-between; font-size:0.85rem; font-weight:600;">
            <span style="display:flex; align-items:center; gap:0.4rem;">
              <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:${vn.color};"></span>
              <span>${isFa ? vn.label_fa : vn.label_en}</span>
            </span>
            <span>${vn.percentage}% (${vn.count})</span>
          </div>
          <div style="width:100%; height:6px; background:var(--badge-bg); border-radius:9999px; overflow:hidden;">
            <div style="width:${vn.percentage}%; height:100%; background:${vn.color}; border-radius:9999px;"></div>
          </div>
        </div>
      `).join('');
    }

    // 4. Research Competency Radar Chart
    else if (state.activeChartTab === 'radar') {
      const items = analytics.radar_competencies;
      const cx = 170;
      const cy = 140;
      const maxR = 95;
      const n = items.length;

      // Concentric background webs (25%, 50%, 75%, 100%)
      let webs = '';
      [0.25, 0.5, 0.75, 1.0].forEach(ratio => {
        let pts = [];
        for (let i = 0; i < n; i++) {
          const angle = i * (2 * Math.PI / n) - Math.PI / 2;
          const x = cx + maxR * ratio * Math.cos(angle);
          const y = cy + maxR * ratio * Math.sin(angle);
          pts.push(`${x},${y}`);
        }
        webs += `<polygon points="${pts.join(' ')}" fill="none" stroke="var(--border-color)" stroke-width="1"/>`;
      });

      // Axis spokes & labels
      let spokes = '';
      let labels = '';
      for (let i = 0; i < n; i++) {
        const angle = i * (2 * Math.PI / n) - Math.PI / 2;
        const x = cx + maxR * Math.cos(angle);
        const y = cy + maxR * Math.sin(angle);
        spokes += `<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="var(--border-color)" stroke-dasharray="3" stroke-width="1"/>`;
        
        // Label position slightly outside
        const lx = cx + (maxR + 18) * Math.cos(angle);
        const ly = cy + (maxR + 18) * Math.sin(angle);
        const textAnchor = Math.abs(Math.cos(angle)) < 0.2 ? 'middle' : (Math.cos(angle) > 0 ? 'start' : 'end');
        labels += `
          <text x="${lx}" y="${ly + 4}" text-anchor="${textAnchor}" font-size="8.5" font-weight="600" fill="var(--text-faint)">
            ${isFa ? items[i].axis_fa : items[i].axis_en}
          </text>
        `;
      }

      // Main polygon
      let polyPts = [];
      let dots = '';
      items.forEach((it, i) => {
        const angle = i * (2 * Math.PI / n) - Math.PI / 2;
        const r = (it.score / 100.0) * maxR;
        const x = cx + r * Math.cos(angle);
        const y = cy + r * Math.sin(angle);
        polyPts.push(`${x},${y}`);
        const itLabel = isFa ? it.axis_fa : it.axis_en;
        const tipMsg = `${itLabel}: ${it.score}% ` + (isFa ? 'تسلط علمی' : 'competency');
        dots += `
          <circle cx="${x}" cy="${y}" class="radar-point"
                  data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
          </circle>
        `;
      });

      chartSvgHtml = `
        <svg viewBox="0 0 340 280" style="width:100%; max-width:380px; height:auto; overflow:visible;">
          ${webs}
          ${spokes}
          <polygon points="${polyPts.join(' ')}" class="radar-polygon"/>
          ${dots}
          ${labels}
        </svg>
      `;

      sidebarMetricsHtml = items.map(it => `
        <div class="metric-row">
          <span class="metric-label">${isFa ? it.axis_fa : it.axis_en}</span>
          <span class="metric-value" style="color:var(--primary); font-size:1.05rem;">${it.score}%</span>
        </div>
      `).join('');
    }

    // 5. Global Collaborations Network
    else if (state.activeChartTab === 'collaborations') {
      const collabs = analytics.global_collaborations;
      chartSvgHtml = `
        <div style="display:flex; flex-direction:column; gap:1.2rem; width:100%;">
          ${collabs.map(cb => `
            <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:var(--radius-sm); padding:1.1rem 1.4rem; display:flex; align-items:center; justify-content:space-between; box-shadow:var(--shadow-sm);">
              <div style="display:flex; align-items:center; gap:0.85rem;">
                <span style="font-size:2rem;">${cb.flag}</span>
                <div>
                  <h4 style="font-size:1rem; font-weight:700;">${isFa ? cb.region_fa : cb.region_en}</h4>
                  <span style="font-size:0.8rem; color:var(--text-faint);">${isFa ? 'همکاری بین‌دانشگاهی و مقالات مشترک' : 'Joint research & co-authored literature'}</span>
                </div>
              </div>
              <span class="badge primary" style="font-size:0.85rem; padding:0.35rem 0.85rem;">
                ${cb.papers} ${isFa ? 'مقاله مشترک' : 'papers'}
              </span>
            </div>
          `).join('')}
        </div>
      `;

      sidebarMetricsHtml = `
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'همکاری استرالیا (ولونگونگ):' : 'Australia Collaboration:'}</span>
          <span class="metric-value">14 ${isFa ? 'مقاله' : 'papers'}</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'همکاری آلمان (روستوک/لوبک):' : 'Germany Collaboration:'}</span>
          <span class="metric-value">8 ${isFa ? 'مقاله' : 'papers'}</span>
        </div>
        <div class="metric-row">
          <span class="metric-label">${isFa ? 'همکاری‌های ملی (شریف و رازی):' : 'National (Sharif & Razi):'}</span>
          <span class="metric-value">75+ ${isFa ? 'مقاله' : 'papers'}</span>
        </div>
        <div style="font-size:0.75rem; color:var(--text-faint); margin-top:0.5rem; text-align:center;">
          ${isFa ? 'شبکه ارتباطات علمی استاد با پژوهشگران برجسته بین‌المللی در ۳ قاره جهان.' : 'Decades of sustained international academic co-authorship across three continents.'}
        </div>
      `;
    }

    container.innerHTML = `
      <div class="chart-suite-card">
        <!-- Interactive Tabs Switcher -->
        <div class="chart-nav-tabs">
          ${tabsHtml}
        </div>

        <!-- Chart Grid Display -->
        <div class="chart-display-grid">
          <div class="chart-canvas-wrapper" id="chart-stage">
            ${chartSvgHtml}
            <div id="chart-tooltip" class="chart-tooltip-box"></div>
          </div>
          <div class="chart-metrics-sidebar">
            ${sidebarMetricsHtml}
          </div>
        </div>
      </div>
    `;
  }

  // --- Tooltip Handler ---
  window.showChartTooltip = function (e, text) {
    const tip = document.getElementById('chart-tooltip');
    if (!tip) return;
    const stage = document.getElementById('chart-stage');
    if (!stage) return;

    const rect = stage.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    tip.textContent = text;
    tip.style.left = `${x}px`;
    tip.style.top = `${y}px`;
    tip.classList.add('visible');

    e.target.onmouseleave = () => {
      tip.classList.remove('visible');
    };
  };

  // --- Switch Chart Tab ---
  window.switchChartTab = function (tabId) {
    state.activeChartTab = tabId;
    renderInteractiveChartSuite();
  };

  // --- Filter By Year (from chart bar click) ---
  window.filterByYear = function (year) {
    state.pubSearch = String(year);
    const searchInput = document.getElementById('pub-search-input');
    if (searchInput) searchInput.value = String(year);
    renderPublicationsPage();
    showToast(`${state.lang === 'fa' ? 'فیلتر مقالات سال' : 'Filtered for year'} ${year}`);
  };

  // --- Filter By Topic (from domain bar click) ---
  window.filterByTopic = function (topicKey) {
    state.pubTopic = topicKey;
    const topicSelect = document.getElementById('topic-filter-select');
    if (topicSelect) topicSelect.value = topicKey;
    renderPublicationsPage();
    const domainObj = window.ACADEMIC_DATA.analytics.domain_distribution.find(d => d.key === topicKey);
    const label = domainObj ? (state.lang === 'fa' ? domainObj.name_fa : domainObj.name_en) : topicKey;
    showToast(`${state.lang === 'fa' ? 'فیلتر حوزه تخصصی:' : 'Filtered topic:'} ${label}`);
    const feed = document.getElementById('publications-feed');
    if (feed) {
      feed.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  // --- Theses Interactive Filters ---
  window.filterByThesesYear = function (year) {
    state.thesisYear = String(year);
    document.querySelectorAll('[data-thesis-year]').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-thesis-year') === String(year));
    });
    renderThesesPage();
    showToast(`${state.lang === 'fa' ? 'فیلتر پایان‌نامه‌های سال' : 'Filtered theses for year'} ${year}`);
    const grid = document.getElementById('theses-grid');
    if (grid) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  window.filterByThesesTopic = function (topicKey) {
    const topicKeywords = {
      medical: ['پزشکی', 'سی تی', 'سونوگرافی', 'پانکراس', 'کبد', 'سرطان', 'CT', 'Ultrasound', 'Medical', 'Pancreas', 'Liver', 'Cancer'],
      vision: ['تصویر', 'بینایی', 'چهره', 'حرکت', 'Image', 'Vision', 'Face', 'Emotion', 'Detection', 'YOLO'],
      distributed: ['مه', 'ابری', 'توزیع', 'زمان‌بندی', 'Fog', 'Cloud', 'Distributed', 'Scheduling', 'Load'],
      nlp: ['متن', 'احساس', 'فارسی', 'زبان', 'NLP', 'Text', 'Sentiment', 'Language', 'Persian'],
      optimization: ['بهینه‌سازی', 'ملخ', 'الگوریتم', 'Optimization', 'Grasshopper', 'Algorithm', 'PSO']
    };

    const words = topicKeywords[topicKey] || [];
    state.thesisSearch = words[0] || '';
    const input = document.getElementById('thesis-search-input');
    if (input) input.value = state.thesisSearch;
    state.thesisYear = 'all';
    document.querySelectorAll('[data-thesis-year]').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-thesis-year') === 'all');
    });
    renderThesesPage();
    showToast(`${state.lang === 'fa' ? 'فیلتر پایان‌نامه‌های حوزه' : 'Filtered theses in'} ${words[0]}`);
    const grid = document.getElementById('theses-grid');
    if (grid) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  window.resetThesesFilter = function () {
    state.thesisYear = 'all';
    state.thesisSearch = '';
    const input = document.getElementById('thesis-search-input');
    if (input) input.value = '';
    document.querySelectorAll('[data-thesis-year]').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-thesis-year') === 'all');
    });
    renderThesesPage();
    showToast(state.lang === 'fa' ? 'فیلتر پایان‌نامه‌ها بازنشانی شد.' : 'All theses filters reset.');
  };

  // =========================================================================
  // ADDITIONAL INTERACTIVE CHARTS (Home, Theses, Experience, Projects)
  // =========================================================================

  // 1. Executive Research Impact Showcase (for Home Page index.html)
  function renderHomeAnalyticsShowcase() {
    const container = document.getElementById('home-analytics-showcase');
    if (!container) return;

    const isFa = state.lang === 'fa';
    const analytics = window.ACADEMIC_DATA.analytics;

    // Radar SVG for Home
    const radarItems = analytics.radar_competencies;
    const rcx = 160;
    const rcy = 135;
    const maxR = 85;
    const n = radarItems.length;

    let webs = '';
    [0.25, 0.5, 0.75, 1.0].forEach(ratio => {
      let pts = [];
      for (let i = 0; i < n; i++) {
        const angle = i * (2 * Math.PI / n) - Math.PI / 2;
        const x = rcx + maxR * ratio * Math.cos(angle);
        const y = rcy + maxR * ratio * Math.sin(angle);
        pts.push(`${x},${y}`);
      }
      webs += `<polygon points="${pts.join(' ')}" fill="none" stroke="var(--border-color)" stroke-width="1"/>`;
    });

    let spokes = '';
    let labels = '';
    for (let i = 0; i < n; i++) {
      const angle = i * (2 * Math.PI / n) - Math.PI / 2;
      const x = rcx + maxR * Math.cos(angle);
      const y = rcy + maxR * Math.sin(angle);
      spokes += `<line x1="${rcx}" y1="${rcy}" x2="${x}" y2="${y}" stroke="var(--border-color)" stroke-dasharray="3" stroke-width="1"/>`;
      
      const lx = rcx + (maxR + 18) * Math.cos(angle);
      const ly = rcy + (maxR + 18) * Math.sin(angle);
      const textAnchor = Math.abs(Math.cos(angle)) < 0.2 ? 'middle' : (Math.cos(angle) > 0 ? 'start' : 'end');
      labels += `
        <text x="${lx}" y="${ly + 4}" text-anchor="${textAnchor}" font-size="8" font-weight="700" fill="var(--text-faint)">
          ${isFa ? radarItems[i].axis_fa : radarItems[i].axis_en}
        </text>
      `;
    }

    let polyPts = [];
    let radarDots = '';
    radarItems.forEach((it, i) => {
      const angle = i * (2 * Math.PI / n) - Math.PI / 2;
      const r = (it.score / 100.0) * maxR;
      const x = rcx + r * Math.cos(angle);
      const y = rcy + r * Math.sin(angle);
      polyPts.push(`${x},${y}`);
      const hLabel = isFa ? it.axis_fa : it.axis_en;
      const tipMsg = `${hLabel}: ${it.score}% ` + (isFa ? 'تسلط علمی' : 'competency');
      radarDots += `
        <circle cx="${x}" cy="${y}" class="radar-point"
                data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
        </circle>
      `;
    });

    const radarSvg = `
      <svg viewBox="0 0 320 270" style="width:100%; max-width:340px; height:auto; overflow:visible; margin:0 auto; display:block;">
        ${webs}
        ${spokes}
        <polygon points="${polyPts.join(' ')}" class="radar-polygon"/>
        ${radarDots}
        ${labels}
      </svg>
    `;

    // Citations Curve SVG for Home
    const citData = analytics.citations_trajectory;
    const cWidth = 460;
    const cHeight = 200;
    const cPadLeft = 38;
    const cPadBottom = 26;
    const cPadTop = 15;
    const cPadRight = 15;
    const maxC = 1500;
    const stepX = (cWidth - cPadLeft - cPadRight) / (citData.length - 1);

    let cPoly = [`${cPadLeft},${cHeight - cPadBottom}`];
    let cLine = [];
    let cDots = '';

    citData.forEach((d, i) => {
      const x = cPadLeft + i * stepX;
      const y = cHeight - cPadBottom - ((d.cumulative / maxC) * (cHeight - cPadBottom - cPadTop));
      cPoly.push(`${x},${y}`);
      cLine.push(`${x},${y}`);
      const tipMsg = `${d.year}: ${d.cumulative.toLocaleString()} ` + (isFa ? `استناد (+${d.annual})` : `citations (+${d.annual})`);
      cDots += `
        <circle cx="${x}" cy="${y}" class="area-point"
                data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
        </circle>
        ${(i % 3 === 0 || i === citData.length - 1) ? `
          <text x="${x}" y="${cHeight - 8}" text-anchor="middle" font-size="8.5" fill="var(--text-faint)">${d.year}</text>
        ` : ''}
      `;
    });
    cPoly.push(`${cPadLeft + (citData.length - 1) * stepX},${cHeight - cPadBottom}`);

    const citSvg = `
      <svg viewBox="0 0 ${cWidth} ${cHeight}" style="width:100%; height:auto; overflow:visible;">
        <defs>
          <linearGradient id="homeCitGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="var(--cyan)" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="var(--cyan)" stop-opacity="0.0"/>
          </linearGradient>
        </defs>
        <line x1="${cPadLeft}" y1="${cHeight - cPadBottom}" x2="${cWidth - cPadRight}" y2="${cHeight - cPadBottom}" stroke="var(--border-color)" stroke-width="1"/>
        <line x1="${cPadLeft}" y1="${cHeight - cPadBottom - (cHeight - cPadBottom - cPadTop) * 0.5}" x2="${cWidth - cPadRight}" y2="${cHeight - cPadBottom - (cHeight - cPadBottom - cPadTop) * 0.5}" stroke="var(--border-color)" stroke-dasharray="3" stroke-width="1"/>
        <text x="${cPadLeft - 5}" y="${cHeight - cPadBottom - (cHeight - cPadBottom - cPadTop) * 0.5 + 3}" text-anchor="end" font-size="7.5" fill="var(--text-faint)">750</text>
        <text x="${cPadLeft - 5}" y="${cPadTop + 6}" text-anchor="end" font-size="7.5" fill="var(--text-faint)">1,500</text>
        <polygon points="${cPoly.join(' ')}" fill="url(#homeCitGrad)"/>
        <polyline points="${cLine.join(' ')}" class="area-line"/>
        ${cDots}
      </svg>
    `;

    container.innerHTML = `
      <div class="home-charts-grid">
        
        <!-- Card 1: Radar Chart -->
        <div class="analytics-card" id="home-radar-stage">
          <div class="analytics-card-header">
            <div class="analytics-card-title">
              <span>🕸️</span>
              <span>${isFa ? 'رادار شایستگی‌های هوش مصنوعی و تخصص‌های علمی' : 'AI Competency & Research Mastery Radar'}</span>
            </div>
            <span class="analytics-card-badge">${isFa ? '۶ محور بنیادین' : '6 Core Axes'}</span>
          </div>
          <div style="position:relative; width:100%; min-height:260px; display:flex; align-items:center; justify-content:center;">
            ${radarSvg}
          </div>
          <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center; margin-top:0.75rem;">
            <span class="badge primary" style="font-size:0.72rem;">DenseNet121 CT</span>
            <span class="badge cyan" style="font-size:0.72rem;">Federated DACS</span>
            <span class="badge emerald" style="font-size:0.72rem;">Bi-LSTM NLP</span>
            <span class="badge" style="font-size:0.72rem; background:rgba(236,72,153,0.15); color:#ec4899;">Cloud-Fog</span>
          </div>
        </div>

        <!-- Card 2: Citations Curve -->
        <div class="analytics-card" id="home-cit-stage">
          <div class="analytics-card-header">
            <div class="analytics-card-title">
              <span>📈</span>
              <span>${isFa ? 'شتاب رشد استنادات در گوگل اسکولار (۱,۴۱۲+ استناد)' : 'Google Scholar Citations Acceleration Curve'}</span>
            </div>
            <span class="analytics-card-badge" style="color:var(--emerald); background:rgba(16,185,129,0.12);">
              ${isFa ? 'رشد ۵۴٪ اخیر' : '+54% Recent Growth'}
            </span>
          </div>
          <div style="position:relative; width:100%; min-height:200px; display:flex; align-items:center; justify-content:center;">
            ${citSvg}
          </div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:0.5rem; margin-top:1rem; padding-top:0.75rem; border-top:1px solid var(--border-color); text-align:center;">
            <div>
              <div style="font-size:1.15rem; font-weight:800; color:var(--cyan);">1,412+</div>
              <div style="font-size:0.72rem; color:var(--text-faint);">${isFa ? 'استنادات کل' : 'Total Citations'}</div>
            </div>
            <div>
              <div style="font-size:1.15rem; font-weight:800; color:var(--primary);">18</div>
              <div style="font-size:0.72rem; color:var(--text-faint);">${isFa ? 'شاخص h-index' : 'h-index'}</div>
            </div>
            <div>
              <div style="font-size:1.15rem; font-weight:800; color:var(--emerald);">31</div>
              <div style="font-size:0.72rem; color:var(--text-faint);">${isFa ? 'شاخص i10-index' : 'i10-index'}</div>
            </div>
          </div>
        </div>

      </div>
    `;
  }

  // 2. Interactive Theses Analytics Deck (for Theses Page theses.html)
  function renderThesesAnalytics() {
    const container = document.getElementById('theses-analytics-container');
    if (!container) return;

    const isFa = state.lang === 'fa';

    const topicStats = [
      { key: 'medical', icon: '🏥', label_fa: 'هوش مصنوعی و تصاویر پزشکی بالینی', label_en: 'Medical AI & Healthcare Imaging', count: 22, pct: 35, color: 'var(--cyan)' },
      { key: 'vision', icon: '👁️', label_fa: 'یادگیری عمیق، بینایی و بیومتریک', label_en: 'Deep Learning, Vision & Biometrics', count: 18, pct: 25, color: 'var(--primary)' },
      { key: 'distributed', icon: '☁️', label_fa: 'سیستم‌های توزیع‌شده، محاسبات ابری و مه', label_en: 'Distributed, Cloud & Fog Systems', count: 12, pct: 15, color: 'var(--amber)' },
      { key: 'nlp', icon: '💬', label_fa: 'پردازش زبان طبیعی و تحلیل متن', label_en: 'NLP & Text Sentiment Analysis', count: 12, pct: 15, color: '#ec4899' },
      { key: 'optimization', icon: '⚡', label_fa: 'بهینه‌سازی هوشمند و فراابتکاری', label_en: 'Metaheuristics & Optimization', count: 8, pct: 10, color: 'var(--emerald)' }
    ];

    const yearsData = [
      { year: 2026, count: 6 },
      { year: 2025, count: 4 },
      { year: 2024, count: 1 },
      { year: 2023, count: 2 },
      { year: 2022, count: 2 },
      { year: 2021, count: 1 },
      { year: 2020, count: 1 },
      { year: 2019, count: 1 },
      { year: 2018, count: 1 },
      { year: 2017, count: 2 },
      { year: 2016, count: 2 }
    ];

    const tWidth = 460;
    const tHeight = 170;
    const tPadLeft = 25;
    const tPadBottom = 26;
    const tPadTop = 15;
    const tPadRight = 15;
    const maxTh = 7;
    const barW = Math.floor((tWidth - tPadLeft - tPadRight) / yearsData.length) - 6;

    let bars = '';
    yearsData.forEach((d, i) => {
      const x = tPadLeft + i * (barW + 6);
      const barH = ((tHeight - tPadBottom - tPadTop) * d.count) / maxTh;
      const y = tHeight - tPadBottom - barH;
      const tipMsg = `${d.year}: ${d.count} ` + (isFa ? 'پایان‌نامه (کلیک برای فیلتر)' : 'theses (click to filter)');
      bars += `
        <g class="chart-bar-group" onclick="window.filterByThesesYear(${d.year})" style="cursor:pointer;">
          <rect x="${x}" y="${y}" width="${barW}" height="${barH}" rx="3" fill="var(--primary)" opacity="0.85"
                data-tip="${tipMsg}" onmouseenter="window.showChartTooltip(event, this.getAttribute('data-tip'))">
          </rect>
          <text x="${x + barW / 2}" y="${tHeight - 8}" text-anchor="middle" font-size="8.5" fill="var(--text-faint)">${d.year}</text>
          <text x="${x + barW / 2}" y="${y - 4}" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--text-main)">${d.count}</text>
        </g>
      `;
    });

    const thesesSvg = `
      <svg viewBox="0 0 ${tWidth} ${tHeight}" style="width:100%; height:auto; overflow:visible;">
        <line x1="${tPadLeft}" y1="${tHeight - tPadBottom}" x2="${tWidth - tPadRight}" y2="${tHeight - tPadBottom}" stroke="var(--border-color)" stroke-width="1"/>
        ${bars}
      </svg>
    `;

    const topicButtonsHtml = topicStats.map(ts => `
      <button class="theses-topic-pill-btn" onclick="window.filterByThesesTopic('${ts.key}')" title="${isFa ? 'کلیک برای فیلتر پایان‌نامه‌های این حوزه' : 'Click to filter theses in this field'}">
        <span style="display:flex; align-items:center; gap:0.5rem;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:${ts.color};"></span>
          <span>${ts.icon} ${isFa ? ts.label_fa : ts.label_en}</span>
        </span>
        <span style="font-weight:800; color:${ts.color};">${ts.pct}% (${ts.count})</span>
      </button>
    `).join('');

    container.innerHTML = `
      <div class="theses-analytics-grid">
        
        <!-- Thematic Card -->
        <div class="analytics-card">
          <div class="analytics-card-header">
            <div class="analytics-card-title">
              <span>🎯</span>
              <span>${isFa ? 'توزیع موضوعی ۸۵+ پایان‌نامه هدایت‌شده' : 'Thematic Breakdown of 85+ Supervised Theses'}</span>
            </div>
            <span class="analytics-card-badge">${isFa ? 'کلیک برای فیلتر' : 'Click to Filter'}</span>
          </div>
          <div style="display:flex; flex-direction:column; gap:0.5rem;">
            ${topicButtonsHtml}
          </div>
        </div>

        <!-- Yearly Trend Card -->
        <div class="analytics-card" id="theses-chart-stage">
          <div class="analytics-card-header">
            <div class="analytics-card-title">
              <span>📅</span>
              <span>${isFa ? 'روند سالانه فارغ‌التحصیلی و دفاع پایان‌نامه‌ها' : 'Annual Graduation & Defense Velocity'}</span>
            </div>
            <button class="btn-sm" onclick="window.resetThesesFilter()" style="font-size:0.75rem;">
              ${isFa ? 'نمایش همه' : 'Reset Filter'}
            </button>
          </div>
          <div style="position:relative; width:100%; min-height:170px; display:flex; align-items:center; justify-content:center;">
            ${thesesSvg}
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.75rem; padding-top:0.75rem; border-top:1px solid var(--border-color); font-size:0.8rem; color:var(--text-muted);">
            <span>${isFa ? 'دانشجویان دوره اخیر (۲۰۲۴–۲۰۲۶):' : 'Recent Cohort (2024–2026):'}</span>
            <span style="font-weight:800; color:var(--emerald);">16 ${isFa ? 'پایان‌نامه' : 'theses'}</span>
          </div>
        </div>

      </div>
    `;
  }

  // 3. Academic Career & Leadership Milestones Visualizer (for Experience Page experience.html)
  function renderExperienceAnalytics() {
    const container = document.getElementById('experience-analytics-container');
    if (!container) return;

    const isFa = state.lang === 'fa';
    const epochs = [
      {
        icon: '🏛️',
        title_fa: '۱۵ سال ریاست مرکز کامپیوتر، اینترنت و فناوری اطلاعات دانشگاه رازی',
        title_en: '15 Years Head of Computing, Internet & IT Center (Razi University)',
        period: '1999 – 2014 (1378 – 1393)',
        years: 15,
        pct: 50,
        desc_fa: 'طراحی، اجرا و توسعه زیرساخت فیبر نوری پردیس، ۳ دیتاسنتر اختصاصی، کلاستر محاسبات سریع HPC، و اتوماسیون جامع دانشجویی.',
        desc_en: 'Designed campus high-speed fiber-optic network, 3 enterprise data centers, HPC compute cluster, and unified academic portals.',
        color: 'var(--primary)'
      },
      {
        icon: '🎓',
        title_fa: '۵ سال مدیریت گروه مهندسی کامپیوتر و فناوری اطلاعات',
        title_en: '5 Years Head of Computer Engineering Department',
        period: '1996 – 2018 (1375 – 1397 متناوب)',
        years: 5,
        pct: 17,
        desc_fa: 'راه‌اندازی و توسعه مقاطع کارشناسی ارشد و دکتری هوش مصنوعی، جذب اعضای هیئت علمی نخبه و تجهیز آزمایشگاه‌های تخصصی.',
        desc_en: 'Established M.Sc. and Ph.D. graduate programs, recruited top faculty, and equipped specialized research laboratories.',
        color: 'var(--cyan)'
      },
      {
        icon: '🌏',
        title_fa: '۴ سال دوره دکتری و پژوهشگر بین‌المللی در دانشگاه ولونگونگ استرالیا',
        title_en: '4 Years Ph.D. Research Fellow (University of Wollongong, Australia)',
        period: '2001 – 2005 (1380 – 1384)',
        years: 4,
        pct: 14,
        desc_fa: 'اخذ بورسیه دولتی دکتری؛ ارائه الگوریتم‌های نوآورانه در بازیابی تصویر، افرازبندی زاویه‌ای و توصیف کانتورهای هندسی.',
        desc_en: 'Recipient of doctoral scholarship; authored breakthrough algorithms in sketch-based image retrieval and contour analysis.',
        color: 'var(--emerald)'
      },
      {
        icon: '🔬',
        title_fa: '۳۰+ سال تدریس و عضویت مستمر هیئت علمی دانشگاه رازی',
        title_en: '30+ Years Continuous Academic Instruction & Research Faculty',
        period: '1995 – Present (1374 – اکنون)',
        years: 30,
        pct: 100,
        desc_fa: 'آموزش و پرورش هزاران مهندس و پژوهشگر ارشد و دکتری؛ هدایت بیش از ۸۵ پایان‌نامه و انتشار ۱۱۰+ مقاله معتبر بین‌المللی.',
        desc_en: 'Mentored generations of computer engineers; guided 85+ theses and authored 110+ international publications.',
        color: '#8b5cf6'
      }
    ];

    const epochsHtml = epochs.map(ep => `
      <div class="epoch-item">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.4rem;">
          <h4 style="font-size:0.96rem; font-weight:800; display:flex; align-items:center; gap:0.45rem; color:var(--text-main);">
            <span>${ep.icon}</span>
            <span>${isFa ? ep.title_fa : ep.title_en}</span>
          </h4>
          <span class="badge primary" style="font-size:0.76rem;">${ep.period}</span>
        </div>
        <p style="font-size:0.84rem; color:var(--text-muted); line-height:1.6; margin:0.25rem 0;">
          ${isFa ? ep.desc_fa : ep.desc_en}
        </p>
        <div class="epoch-bar-wrapper">
          <div class="epoch-bar-track">
            <div class="epoch-bar-fill" style="width:${ep.pct}%; background:${ep.color};"></div>
          </div>
          <span style="font-size:0.8rem; font-weight:700; color:${ep.color}; min-width:60px; text-align:left;">${ep.years} ${isFa ? 'سال' : 'years'}</span>
        </div>
      </div>
    `).join('');

    container.innerHTML = `
      <div class="analytics-card">
        <div class="analytics-card-header">
          <div class="analytics-card-title">
            <span>⏱️</span>
            <span>${isFa ? 'نقشه زمانی سوابق علمی، دانشگاهی و مسئولیت‌های کلان مدیریتی' : 'Academic Leadership & Career Milestones Allocation'}</span>
          </div>
          <span class="analytics-card-badge">${isFa ? 'بیش از ۳ دهه خدمت علمی' : '3+ Decades in Academia'}</span>
        </div>
        <div class="epochs-container">
          ${epochsHtml}
        </div>
      </div>
    `;
  }

  // 4. Innovation Matrix & Applied Grants (for Projects Page projects.html)
  function renderProjectsAnalytics() {
    const container = document.getElementById('projects-analytics-container');
    if (!container) return;

    const isFa = state.lang === 'fa';

    container.innerHTML = `
      <div class="innovation-grid">
        
        <div class="innovation-stat-card">
          <div style="font-size:1.8rem;">📜</div>
          <div style="display:flex; justify-content:space-between; align-items:baseline;">
            <span style="font-size:1.6rem; font-weight:800; color:var(--emerald);">۲</span>
            <span class="badge emerald">TRL 7–8</span>
          </div>
          <h4 style="font-size:0.95rem; font-weight:800;">${isFa ? 'ثبت اختراع رسمی ملی' : 'National Registered Patents'}</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.5;">
            ${isFa ? 'ثبت‌شده در اداره کل مالکیت صنعتی: دستگاه قرائت اپتیکی ارقام کنتور و ترمینال امن پرداخت بدون کارت.' : 'Registered with State Deeds Office: Embedded OCR meter reader and cardless payment terminal.'}
          </p>
        </div>

        <div class="innovation-stat-card">
          <div style="font-size:1.8rem;">🏭</div>
          <div style="display:flex; justify-content:space-between; align-items:baseline;">
            <span style="font-size:1.6rem; font-weight:800; color:var(--primary);">۷</span>
            <span class="badge primary">${isFa ? 'قرارداد صنعتی' : 'Industrial Contracts'}</span>
          </div>
          <h4 style="font-size:0.95rem; font-weight:800;">${isFa ? 'طرح‌های کاربردی ارتباط با صنعت' : 'Applied Industrial Research Grants'}</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.5;">
            ${isFa ? 'همکاری‌های تقاضامحور با وزارت نیرو، شرکت‌های توزیع نیروی برق و مخابرات در زمینه بینایی ماشین و هوشمندسازی.' : 'Industry partnerships with Ministry of Energy and Telecom in computer vision and grid optimization.'}
          </p>
        </div>

        <div class="innovation-stat-card">
          <div style="font-size:1.8rem;">💡</div>
          <div style="display:flex; justify-content:space-between; align-items:baseline;">
            <span style="font-size:1.6rem; font-weight:800; color:var(--cyan);">۱۰۰٪</span>
            <span class="badge cyan">${isFa ? 'توسعه بومی' : 'Indigenous Tech'}</span>
          </div>
          <h4 style="font-size:0.95rem; font-weight:800;">${isFa ? 'کاربردپذیری و ارزش صنعتی' : 'Commercial & Applied Utility'}</h4>
          <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.5;">
            ${isFa ? 'تمامی پروژه‌ها دارای نمونه سخت‌افزاری تعبیه‌شده یا نرم‌افزار عملیاتی پیاده‌سازی‌شده در مقیاس کاربردی هستند.' : 'All projects feature embedded hardware prototypes or operational software deployed in real-world scenarios.'}
          </p>
        </div>

      </div>
    `;
  }

  // =========================================================================
  // PAGE RENDERERS
  // =========================================================================

  // 1. Home Page Renderer
  function renderHomePage() {
    const profile = window.ACADEMIC_DATA.profile;
    const isFa = state.lang === 'fa';

    const heroAvatarImg = document.getElementById('hero-avatar-img');
    const heroTitle = document.getElementById('hero-title');
    const heroRank = document.getElementById('hero-rank');
    const heroDept = document.getElementById('hero-dept');
    const heroBio = document.getElementById('hero-bio');
    const heroQuote = document.getElementById('hero-quote');
    const heroVerified = document.getElementById('hero-verified-text');

    if (heroAvatarImg) heroAvatarImg.src = profile.photo;
    if (heroTitle) heroTitle.textContent = isFa ? profile.name.fa : profile.name.en;
    if (heroRank) heroRank.textContent = isFa ? profile.title.fa : profile.title.en;
    if (heroDept) {
      heroDept.innerHTML = `
        <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
        </svg>
        <span>${isFa ? profile.affiliation.fa : profile.affiliation.en}</span>
      `;
    }
    if (heroBio) heroBio.textContent = isFa ? profile.bio.fa : profile.bio.en;
    if (heroQuote) heroQuote.textContent = isFa ? profile.personal_quote.fa : profile.personal_quote.en;
    if (heroVerified) heroVerified.textContent = t('verified_prof');

    // Stats Grid
    const s = profile.stats;
    const statsGrid = document.getElementById('stats-grid');
    if (statsGrid) {
      const statsData = [
        { val: `${s.citations.toLocaleString()}+`, label: t('citations_label'), sub: isFa ? `(${s.recent_citations} پس از ۲۰۱۹)` : `(${s.recent_citations} since 2019)` },
        { val: s.h_index, label: t('hindex_label'), sub: isFa ? `(${s.recent_h_index} اخیر)` : `(${s.recent_h_index} recent)` },
        { val: s.i10_index, label: t('i10index_label'), sub: isFa ? `(${s.recent_i10_index} اخیر)` : `(${s.recent_i10_index} recent)` },
        { val: `${s.publications_count}+`, label: t('pubs_label'), sub: isFa ? "مجلات و همایش‌ها" : "Journals & Confs" },
        { val: `${s.theses_count}+`, label: t('theses_label'), sub: isFa ? "پایان‌نامه ارشد و دکتری" : "M.Sc. & Ph.D." },
        { val: `${s.experience_years}+`, label: t('exp_label'), sub: isFa ? "سابقه دانشگاهی" : "Years Academic" }
      ];
      statsGrid.innerHTML = statsData.map(st => `
        <div class="stat-box">
          <div class="stat-num">${st.val}</div>
          <div class="stat-label">${st.label}</div>
          <div class="stat-sub">${st.sub}</div>
        </div>
      `).join('');
    }

    // Core Research Pillars
    const pillarsGrid = document.getElementById('pillars-grid');
    if (pillarsGrid) {
      const interests = window.ACADEMIC_DATA.research_interests;
      pillarsGrid.innerHTML = interests.map(item => `
        <div class="pillar-card">
          <div class="pillar-icon">🔬</div>
          <h4 class="pillar-title">${isFa ? item.title_fa : item.title_en}</h4>
          <p class="pillar-desc">${isFa ? item.desc_fa : item.desc_en}</p>
        </div>
      `).join('');
    }

    // Render Home Interactive Research Impact Analytics
    renderHomeAnalyticsShowcase();

    // Recent High-Impact Breakthroughs (Selected 2024–2026 works)
    const featuredList = document.getElementById('featured-pubs-list');
    if (featuredList) {
      const highlights = window.ACADEMIC_DATA.publications.filter(p => p.highlight).slice(0, 4);
      featuredList.innerHTML = highlights.map(pub => {
        const title = isFa ? (pub.title_fa || pub.title_en) : (pub.title_en || pub.title_fa);
        const venue = isFa ? (pub.journal_fa || pub.conference_fa || pub.journal_en) : (pub.journal_en || pub.conference_en);
        const abstract = isFa ? (pub.abstract_fa || pub.abstract_en) : (pub.abstract_en || pub.abstract_fa);
        const authorsFormatted = (pub.authors || '').replace(/(Abdolah\s+CHalehchaleh|Abdolah\s+Chalechale|A\.\s*Chalechale|عبدالله\s+چاله\s*چاله|عبداله\s+چاله\s*چاله)/gi, '<span class="highlight-name">$1</span>');

        return `
          <article class="pub-entry highlight">
            <div class="pub-top-row">
              <div class="pub-tags">
                <span class="year-tag">${pub.year}</span>
                <span class="badge primary">${pub.category === 'journal' ? (isFa ? 'مقاله ژورنال' : 'Journal') : (isFa ? 'کنفرانس' : 'Conference')}</span>
                ${pub.badge ? `<span class="badge emerald">${pub.badge}</span>` : ''}
              </div>
              <div style="display:flex; gap:0.4rem;">
                <button class="btn-sm" onclick="window.copyBibTeX('${pub.id}')">BibTeX</button>
                <button class="btn-sm" onclick="window.copyAPA('${pub.id}')">APA</button>
              </div>
            </div>
            <h4 class="pub-title-text">${title}</h4>
            <div class="pub-authors-text">${authorsFormatted}</div>
            <div class="pub-venue-text">${venue} ${pub.pages ? `· pp. ${pub.pages}` : ''}</div>
            ${abstract ? `<div class="pub-abstract-box">${abstract}</div>` : ''}
          </article>
        `;
      }).join('');
    }
  }

  // 2. Publications Page Renderer
  function renderPublicationsPage() {
    renderSubpageBanner('pubs_page_title', 'pubs_page_subtitle', state.lang === 'fa' ? 'مقالات و پژوهش‌ها' : 'Publications');

    // Render the Advanced Interactive Chart Suite
    renderInteractiveChartSuite();

    const rawList = window.ACADEMIC_DATA.publications;
    const isFa = state.lang === 'fa';
    const container = document.getElementById('publications-feed');
    if (!container) return;

    // Filter by Category
    let filtered = rawList.filter(p => {
      if (state.pubCategory === 'journal' && p.category !== 'journal') return false;
      if (state.pubCategory === 'conference' && p.category !== 'conference') return false;
      if (state.pubCategory === 'highlight' && !p.highlight) return false;
      return true;
    });

    // Filter by Topic
    if (state.pubTopic !== 'all') {
      filtered = filtered.filter(p => p.topic === state.pubTopic);
    }

    // Filter by Search Query
    if (state.pubSearch.trim()) {
      const q = state.pubSearch.toLowerCase().trim();
      filtered = filtered.filter(p => {
        const title = ((p.title_en || '') + ' ' + (p.title_fa || '')).toLowerCase();
        const authors = (p.authors || '').toLowerCase();
        const venue = ((p.journal_en || '') + ' ' + (p.conference_en || '')).toLowerCase();
        const year = String(p.year || '');
        return title.includes(q) || authors.includes(q) || venue.includes(q) || year.includes(q);
      });
    }

    // Sort
    if (state.pubSort === 'newest') {
      filtered.sort((a, b) => b.year - a.year);
    } else if (state.pubSort === 'oldest') {
      filtered.sort((a, b) => a.year - b.year);
    } else if (state.pubSort === 'title') {
      filtered.sort((a, b) => (a.title_en || '').localeCompare(b.title_en || ''));
    }

    if (filtered.length === 0) {
      container.innerHTML = `<div style="text-align:center; padding:3rem; color:var(--text-muted); background:var(--bg-card); border-radius:var(--radius-md); border:1px solid var(--border-color);">${t('no_results')}</div>`;
      return;
    }

    container.innerHTML = filtered.map(pub => {
      const title = isFa ? (pub.title_fa || pub.title_en) : (pub.title_en || pub.title_fa);
      const venue = isFa ? (pub.journal_fa || pub.conference_fa || pub.journal_en || pub.conference_en) : (pub.journal_en || pub.conference_en);
      const abstract = isFa ? (pub.abstract_fa || pub.abstract_en) : (pub.abstract_en || pub.abstract_fa);
      const highlightClass = pub.highlight ? 'highlight' : '';
      const authorsFormatted = (pub.authors || '').replace(/(Abdolah\s+CHalehchaleh|Abdolah\s+Chalechale|A\.\s*Chalechale|عبدالله\s+چاله\s*چاله|عبداله\s+چاله\s*چاله)/gi, '<span class="highlight-name">$1</span>');

      return `
        <article class="pub-entry ${highlightClass}">
          <div class="pub-top-row">
            <div class="pub-tags">
              <span class="year-tag">${pub.year}</span>
              <span class="badge ${pub.category === 'journal' ? 'primary' : 'cyan'}">
                ${pub.category === 'journal' ? (isFa ? 'مقاله ژورنال' : 'Journal Article') : (isFa ? 'کنفرانس بین‌المللی' : 'Conference')}
              </span>
              ${pub.badge ? `<span class="badge emerald">${pub.badge}</span>` : ''}
            </div>
            <div style="display:flex; gap:0.4rem;">
              <button class="btn-sm" onclick="window.copyBibTeX('${pub.id}')">BibTeX</button>
              <button class="btn-sm" onclick="window.copyAPA('${pub.id}')">APA</button>
            </div>
          </div>

          <h3 class="pub-title-text">${title}</h3>
          <div class="pub-authors-text">${authorsFormatted}</div>
          <div class="pub-venue-text">${venue} ${pub.pages ? `· pp. ${pub.pages}` : ''}</div>

          ${abstract ? `<div class="pub-abstract-box">${abstract}</div>` : ''}

          <div class="pub-bot-row">
            <span style="font-size:0.78rem; color:var(--text-faint);">
              ${pub.publisher ? `Publisher: ${pub.publisher}` : ''}
              ${pub.doi ? `· DOI: ${pub.doi}` : ''}
            </span>
            <button class="btn-sm" onclick="window.openPubModal('${pub.id}')">
              ${t('view_abstract')} ↗
            </button>
          </div>
        </article>
      `;
    }).join('');
  }

  // 3. Theses Page Renderer
  function renderThesesPage() {
    renderSubpageBanner('theses_page_title', 'theses_page_subtitle', state.lang === 'fa' ? 'پایان‌نامه‌ها' : 'Theses');
    renderThesesAnalytics();

    const rawList = window.ACADEMIC_DATA.theses;
    const isFa = state.lang === 'fa';
    const container = document.getElementById('theses-grid');
    if (!container) return;

    let filtered = rawList;
    if (state.thesisYear !== 'all') {
      if (state.thesisYear === 'older') {
        filtered = filtered.filter(th => th.year < 2023);
      } else {
        const y = parseInt(state.thesisYear);
        filtered = filtered.filter(th => th.year === y);
      }
    }

    if (state.thesisSearch.trim()) {
      const q = state.thesisSearch.toLowerCase().trim();
      filtered = filtered.filter(th => {
        const str = ((th.title_en || '') + ' ' + (th.title_fa || '') + ' ' + (th.student_en || '') + ' ' + (th.student_fa || '')).toLowerCase();
        return str.includes(q);
      });
    }

    if (filtered.length === 0) {
      container.innerHTML = `<div style="grid-column:1/-1; text-align:center; padding:2.5rem; color:var(--text-muted); background:var(--bg-card); border-radius:var(--radius-md); border:1px solid var(--border-color);">${t('no_results')}</div>`;
      return;
    }

    container.innerHTML = filtered.map(th => `
      <div class="thesis-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="badge primary">${th.degree}</span>
          <span class="year-tag">${th.year}</span>
        </div>
        <div class="thesis-student-row">
          <span>${t('researcher_label')}</span>
          <strong>${isFa ? th.student_fa : th.student_en}</strong>
        </div>
        <h4 class="thesis-title-text">${isFa ? th.title_fa : th.title_en}</h4>
        <p class="thesis-desc">${isFa ? th.abstract_fa : th.abstract_en}</p>
      </div>
    `).join('');
  }

  // 4. Experience & Timeline Page Renderer
  function renderExperiencePage() {
    renderSubpageBanner('exp_page_title', 'exp_page_subtitle', state.lang === 'fa' ? 'سوابق علمی' : 'Experience');
    renderExperienceAnalytics();

    const eduList = window.ACADEMIC_DATA.education;
    const ldrList = window.ACADEMIC_DATA.leadership;
    const isFa = state.lang === 'fa';
    const container = document.getElementById('timeline-nodes');
    if (!container) return;

    const combined = [
      ...ldrList.map(item => ({ ...item, isLeadership: true })),
      ...eduList.map(item => ({ ...item, isLeadership: false }))
    ];

    container.innerHTML = combined.map(item => {
      const title = item.isLeadership ? (isFa ? item.role_fa : item.role_en) : (isFa ? item.degree_fa : item.degree_en);
      const inst = isFa ? item.institution_fa : item.institution_en;
      const desc = item.isLeadership ? (isFa ? item.desc_fa : item.desc_en) : (isFa ? item.details_fa : item.details_en);
      const date = item.period || item.year;

      return `
        <div class="timeline-node">
          <div class="timeline-marker"></div>
          <div class="timeline-box">
            <div class="timeline-year">${date}</div>
            <h3 class="timeline-headline">${title}</h3>
            <div class="timeline-organization">${inst}</div>
            <p class="timeline-narrative">${desc}</p>
          </div>
        </div>
      `;
    }).join('');
  }

  // 5. Teaching & Courses Page Renderer
  function renderTeachingPage() {
    renderSubpageBanner('teaching_page_title', 'teaching_page_subtitle', state.lang === 'fa' ? 'دروس و آموزش' : 'Teaching');

    const courses = window.ACADEMIC_DATA.courses;
    const isFa = state.lang === 'fa';
    const grid = document.getElementById('courses-grid');
    if (!grid) return;

    grid.innerHTML = courses.map(c => `
      <div class="course-box">
        <div class="course-top-meta">
          <span class="badge cyan">${isFa ? c.level_fa : c.level_en}</span>
          <span style="font-size:0.8rem; font-weight:700; color:var(--text-faint);">${c.units} ${t('units_text')}</span>
        </div>
        <h4 class="course-title-text">${isFa ? c.title_fa : c.title_en}</h4>
        <p class="course-info-text">${isFa ? c.desc_fa : c.desc_en}</p>
      </div>
    `).join('');
  }

  // 6. Patents & Projects Page Renderer
  function renderProjectsPage() {
    renderSubpageBanner('projects_page_title', 'projects_page_subtitle', state.lang === 'fa' ? 'اختراعات و پروژه‌ها' : 'Patents');
    renderProjectsAnalytics();

    const patents = window.ACADEMIC_DATA.patents;
    const projects = window.ACADEMIC_DATA.applied_projects;
    const isFa = state.lang === 'fa';
    const grid = document.getElementById('projects-grid');
    if (!grid) return;

    const all = [
      ...patents.map(p => ({ ...p, isPatent: true })),
      ...projects.map(p => ({ ...p, isPatent: false }))
    ];

    grid.innerHTML = all.map(item => {
      const title = isFa ? item.title_fa : item.title_en;
      const desc = isFa ? item.desc_fa : item.desc_en;
      const sub = item.isPatent 
        ? `${isFa ? 'شماره ثبت اختراع:' : 'Patent Reg No:'} ${item.patent_no} (${item.year})` 
        : `${isFa ? item.sponsor_fa : item.sponsor_en} · ${item.year}`;

      return `
        <div class="project-box">
          <span class="badge ${item.isPatent ? 'emerald' : 'primary'}">
            ${item.isPatent ? (isFa ? 'ثبت اختراع رسمی' : 'National Patent') : (isFa ? 'طرح پژوهشی کاربردی' : 'Industrial Grant')}
          </span>
          <h4 class="project-title-text">${title}</h4>
          <div style="font-size:0.8rem; color:var(--text-faint);">${sub}</div>
          <p class="project-info-text">${desc}</p>
        </div>
      `;
    }).join('');
  }

  // 7. Contact Page Renderer
  function renderContactPage() {
    renderSubpageBanner('contact_page_title', 'contact_page_subtitle', state.lang === 'fa' ? 'تماس با استاد' : 'Contact');

    const prof = window.ACADEMIC_DATA.profile;
    const isFa = state.lang === 'fa';

    const officeText = document.getElementById('contact-office-text');
    const emailLink = document.getElementById('contact-email-link');
    const phoneText = document.getElementById('contact-phone-text');

    if (officeText) officeText.textContent = isFa ? prof.office.fa : prof.office.en;
    if (emailLink) {
      emailLink.href = `mailto:${prof.email}`;
      emailLink.textContent = prof.email;
    }
    if (phoneText) phoneText.textContent = prof.phone;
  }

  // --- Master Render Function ---
  function initPage() {
    document.documentElement.setAttribute('data-theme', state.theme);
    document.documentElement.setAttribute('lang', state.lang);
    document.documentElement.setAttribute('dir', state.lang === 'fa' ? 'rtl' : 'ltr');
    document.title = t('site_title');

    renderHeader();
    renderFooter();

    const page = getCurrentPageName();
    if (page === 'home') renderHomePage();
    else if (page === 'publications') renderPublicationsPage();
    else if (page === 'theses') renderThesesPage();
    else if (page === 'experience') renderExperiencePage();
    else if (page === 'teaching') renderTeachingPage();
    else if (page === 'projects') renderProjectsPage();
    else if (page === 'contact') renderContactPage();

    setupListeners();
  }

  // --- Setup Page Listeners ---
  function setupListeners() {
    document.querySelectorAll('[data-pub-filter]').forEach(btn => {
      btn.onclick = () => {
        document.querySelectorAll('[data-pub-filter]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.pubCategory = btn.getAttribute('data-pub-filter');
        renderPublicationsPage();
      };
    });

    const topicSelect = document.getElementById('topic-filter-select');
    if (topicSelect) {
      topicSelect.onchange = (e) => {
        state.pubTopic = e.target.value;
        renderPublicationsPage();
      };
    }

    const sortSelect = document.getElementById('pub-sort-select');
    if (sortSelect) {
      sortSelect.onchange = (e) => {
        state.pubSort = e.target.value;
        renderPublicationsPage();
      };
    }

    const pubSearchInput = document.getElementById('pub-search-input');
    if (pubSearchInput) {
      pubSearchInput.oninput = (e) => {
        state.pubSearch = e.target.value;
        renderPublicationsPage();
      };
    }

    document.querySelectorAll('[data-thesis-year]').forEach(btn => {
      btn.onclick = () => {
        document.querySelectorAll('[data-thesis-year]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.thesisYear = btn.getAttribute('data-thesis-year');
        renderThesesPage();
      };
    });

    const thesisSearchInput = document.getElementById('thesis-search-input');
    if (thesisSearchInput) {
      thesisSearchInput.oninput = (e) => {
        state.thesisSearch = e.target.value;
        renderThesesPage();
      };
    }
  }

  // --- Global Window API ---
  window.toggleLanguage = function () {
    state.lang = state.lang === 'fa' ? 'en' : 'fa';
    localStorage.setItem('chalechale_lang', state.lang);
    initPage();
  };

  window.toggleTheme = function () {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('chalechale_theme', state.theme);
    initPage();
  };

  window.toggleMobileMenu = function () {
    state.mobileMenuOpen = !state.mobileMenuOpen;
    const drawer = document.getElementById('mobile-drawer');
    if (drawer) {
      drawer.classList.toggle('active', state.mobileMenuOpen);
    }
  };

  window.copyBibTeX = function (pubId) {
    const pub = window.ACADEMIC_DATA.publications.find(p => p.id === pubId);
    if (!pub) return;
    const bib = formatBibTeX(pub);
    navigator.clipboard.writeText(bib).then(() => {
      showToast(t('bibtex_copied'));
    }).catch(() => {
      prompt('BibTeX Citation:', bib);
    });
  };

  window.copyAPA = function (pubId) {
    const pub = window.ACADEMIC_DATA.publications.find(p => p.id === pubId);
    if (!pub) return;
    const apa = formatAPA(pub);
    navigator.clipboard.writeText(apa).then(() => {
      showToast(t('apa_copied'));
    }).catch(() => {
      prompt('APA Citation:', apa);
    });
  };

  window.openPubModal = function (pubId) {
    const pub = window.ACADEMIC_DATA.publications.find(p => p.id === pubId);
    if (!pub) return;
    const isFa = state.lang === 'fa';

    const titleEl = document.getElementById('modal-title');
    const authorsEl = document.getElementById('modal-authors');
    const venueEl = document.getElementById('modal-venue');
    const abstractEl = document.getElementById('modal-abstract');
    const bibtexEl = document.getElementById('modal-bibtex');
    const doiBtn = document.getElementById('modal-doi-link');

    if (titleEl) titleEl.textContent = isFa ? (pub.title_fa || pub.title_en) : (pub.title_en || pub.title_fa);
    if (authorsEl) authorsEl.textContent = pub.authors;
    if (venueEl) venueEl.textContent = `${pub.journal_en || pub.conference_en || ''} (${pub.year})`;
    if (abstractEl) abstractEl.textContent = isFa ? (pub.abstract_fa || pub.abstract_en || 'بدون چکیده.') : (pub.abstract_en || pub.abstract_fa || 'No abstract available.');
    if (bibtexEl) bibtexEl.textContent = formatBibTeX(pub);
    if (doiBtn) {
      if (pub.doi) {
        doiBtn.href = `https://doi.org/${pub.doi}`;
        doiBtn.style.display = 'inline-flex';
      } else {
        doiBtn.style.display = 'none';
      }
    }

    const overlay = document.getElementById('pub-modal-overlay');
    if (overlay) overlay.classList.add('active');
  };

  window.closePubModal = function () {
    const overlay = document.getElementById('pub-modal-overlay');
    if (overlay) overlay.classList.remove('active');
  };

  // --- Bootstrap ---
  document.addEventListener('DOMContentLoaded', initPage);

})();
