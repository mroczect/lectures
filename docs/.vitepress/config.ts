import { defineConfig } from 'vitepress';
import { pagefindPlugin } from 'vitepress-plugin-pagefind';
import { withMermaid } from 'vitepress-mermaid-plugin';
import { withPwa } from '@vite-pwa/vitepress';
import llmstxt from 'vitepress-plugin-llms';
import sidebar from './sidebar.json' with { type: 'json' };
import footnote from 'markdown-it-footnote';
import taskLists from 'markdown-it-task-lists';
import abbr from 'markdown-it-abbr';
import deflist from 'markdown-it-deflist';
import mark from 'markdown-it-mark';
import ins from 'markdown-it-ins';
import sub from 'markdown-it-sub';
import sup from 'markdown-it-sup';
import attrs from 'markdown-it-attrs';
import mathjax3 from 'markdown-it-mathjax3';
const SITE_URL = 'https://mroczect.github.io/lectures';
const SITE_NAME = 'Lectures';
const AUTHOR = 'Muhammad Riduwan Khafidi';
const REPO_URL = 'https://github.com/mroczect/lectures.git';
const BASE_PATH = '/lectures/';
export default withPwa(
  withMermaid(
    defineConfig({
      lang: 'id-ID',
      title: SITE_NAME,
      base: BASE_PATH,
      titleTemplate: ':title — Dokumentasi Kuliah',
      description:
        'Dokumentasi lengkap materi kuliah, tugas, dan catatan untuk mahasiswa TRPL Politeknik Negeri Batam.',

      head: [
        [
          'link',
          { rel: 'icon', type: 'image/png', href: '/favicon-96x96.png?v=1', sizes: '96x96' },
        ],
        ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg?v=1' }],
        ['link', { rel: 'shortcut icon', href: '/favicon.ico?v=1' }],
        ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png?v=1' }],
        ['link', { rel: 'manifest', href: '/site.webmanifest?v=1' }],

        // Fonts
        ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
        [
          'link',
          {
            rel: 'preconnect',
            href: 'https://fonts.gstatic.com',
            crossorigin: '',
          },
        ],
        [
          'link',
          {
            rel: 'stylesheet',
            href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap',
          },
        ],

        // Meta
        ['meta', { name: 'author', content: AUTHOR }],
        ['meta', { name: 'theme-color', content: '#3eaf7c' }],
        ['meta', { name: 'viewport', content: 'width=device-width,initial-scale=1' }],
        ['meta', { property: 'og:type', content: 'website' }],
        ['meta', { property: 'og:site_name', content: SITE_NAME }],
        ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
      ],

      cleanUrls: true,
      srcDir: '.',
      srcExclude: ['**/README.md', '**/TODO.md', '**/node_modules/**', '**/.vitepress/**'],
      outDir: './.vitepress/dist',
      cacheDir: './.vitepress/cache',
      assetsDir: 'assets',

      ignoreDeadLinks: [/^https?:\/\/localhost/, '/playground', /^https?:\/\/twitter\.com/],

      appearance: true,
      lastUpdated: true,

      sitemap: {
        hostname: SITE_URL,
      },

      markdown: {
        headers: {
          level: [2, 3, 4],
        },

        theme: {
          light: 'github-light',
          dark: 'github-dark',
        },

        lineNumbers: true,

        anchor: {
          permalink: true,
        },

        toc: {
          level: [2, 3],
        },

        config: (md) => {
          md.use(footnote)
            .use(taskLists, { enabled: true, label: true })
            .use(abbr)
            .use(deflist)
            .use(mark)
            .use(ins)
            .use(sub)
            .use(sup)
            .use(attrs)
            .use(mathjax3);
        },

        image: {
          lazyLoading: true,
        },

        highlightLines: true,

        attrs: {
          leftDelimiter: '{',
          rightDelimiter: '}',
        },
      },

      vite: {
        server: {
          port: 5173,
          host: true,
        },

        build: {
          chunkSizeWarningLimit: 1500,
        },

        ssr: {
          noExternal: ['vitepress-plugin-pagefind'],
        },

        plugins: [
          pagefindPlugin({
            btnPlaceholder: 'Cari',
            placeholder: 'Cari dokumentasi...',
            emptyText: 'Tidak ada hasil',
            heading: 'Total: {{searchResult}} hasil',
            excludeSelector: ['img', 'a.header-anchor', '.vp-doc'],
            forceLanguage: 'id',
            showEmpty: false,
            indexing: {
              start: 'docs',
              glob: '**/*.{md,html}',
            },
          }),

          llmstxt({
            generateLLMsTxt: true,
            generateLLMsFullTxt: true,
          }),
        ],
      },

      async transformHead(context) {
        if (context.page === '404.md') return [];
        return [['meta', { property: 'og:image', content: `${SITE_URL}/og.png` }]];
      },

      async transformPageData(pageData) {
        const isHome = pageData.frontmatter.layout === 'home';
        const title = isHome ? SITE_NAME : `${pageData.title} | ${SITE_NAME}`;

        pageData.frontmatter.head ??= [];
        pageData.frontmatter.head.push(['meta', { property: 'og:title', content: title }]);

        const relativePath = pageData.relativePath
          .replace(/index\.md$/, '')
          .replace(/\.md$/, '.html');
        const canonicalUrl = `${SITE_URL}/${relativePath}`;

        pageData.frontmatter.head.push(['link', { rel: 'canonical', href: canonicalUrl }]);

        return pageData;
      },

      themeConfig: {
        logo: '/favicon.svg',
        siteTitle: SITE_NAME,

        nav: [
          { text: 'Beranda', link: '/' },
          { text: 'Mata Kuliah', link: '/courses/' },
          { text: 'Informasi', link: '/information/' },
          { text: 'Tugas', link: '/task/' },
          { text: 'Tentang', link: '/about' },
        ],

        sidebar,

        socialLinks: [{ icon: 'github', link: REPO_URL }],

        footer: {
          message: 'Dirilis di bawah Lisensi MIT.',
          copyright: `Copyright © 2026-present ${AUTHOR}`,
        },

        editLink: {
          pattern: `${REPO_URL}/edit/main/docs/:path`,
          text: 'Edit halaman ini di GitHub',
        },

        lastUpdated: {
          text: 'Terakhir diperbarui',
          formatOptions: {
            dateStyle: 'short',
            timeStyle: 'medium',
            forceLocale: true,
          },
        },

        search: {
          provider: 'local',
          options: {
            translations: {
              button: {
                buttonText: 'Cari',
                buttonAriaLabel: 'Cari',
              },
              modal: {
                displayDetails: 'Tampilkan daftar lengkap',
                resetButtonTitle: 'Reset pencarian',
                backButtonTitle: 'Tutup pencarian',
                noResultsText: 'Tidak ada hasil',
                footer: {
                  selectText: 'Pilih',
                  selectKeyAriaLabel: 'Enter',
                  navigateText: 'Navigasi',
                  navigateUpKeyAriaLabel: 'Panah atas',
                  navigateDownKeyAriaLabel: 'Panah bawah',
                  closeText: 'Tutup',
                  closeKeyAriaLabel: 'Esc',
                },
              },
            },
            miniSearch: {
              searchOptions: {
                fuzzy: 0.2,
                prefix: true,
                boost: { title: 4, text: 2, titles: 1 },
              },
            },
            detailedView: true,
          },
        },

        docFooter: {
          prev: 'Sebelumnya',
          next: 'Berikutnya',
        },

        outline: {
          level: [2, 3],
          label: 'Di halaman ini',
        },

        darkModeSwitchLabel: 'Tema',
        lightModeSwitchTitle: 'Ganti ke mode terang',
        darkModeSwitchTitle: 'Ganti ke mode gelap',

        sidebarMenuLabel: 'Menu',
        returnToTopLabel: 'Kembali ke atas',
        langMenuLabel: 'Ganti bahasa',
        externalLinkIcon: true,

        notFound: {
          title: 'Halaman Tidak Ditemukan',
          quote:
            'Tapi jika kamu tidak mengubah arah, dan terus mencari, kamu mungkin akan berakhir di tempat yang kamu tuju.',
          linkLabel: 'ke beranda',
          linkText: 'Bawa saya ke beranda',
        },
      },
    })
  )
);
