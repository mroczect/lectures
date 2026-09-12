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

const withBase = (path: string) => `${BASE_PATH}${path.replace(/^\/+/, '')}`;

type Version = {
  key: string;
  label: string;
  link: string;
  badge?: string;
};

const VERSIONS: Version[] = [{ key: 'v1', label: 'v1', link: '/v1/', badge: 'latest' }];

export default withPwa(
  withMermaid(
    defineConfig({
      lang: 'en-US',
      title: SITE_NAME,
      base: BASE_PATH,
      titleTemplate: ':title - Lecture Documentation',
      description:
        'Complete documentation of lecture materials, assignments, and notes for students of Software Engineering Technology at Politeknik Negeri Batam.',

      head: [
        [
          'link',
          {
            rel: 'icon',
            type: 'image/png',
            href: withBase('favicon-96x96.png?v=1'),
            sizes: '96x96',
          },
        ],
        ['link', { rel: 'icon', type: 'image/svg+xml', href: withBase('favicon.svg') }],
        ['link', { rel: 'shortcut icon', href: withBase('favicon.ico?v=1') }],
        [
          'link',
          {
            rel: 'apple-touch-icon',
            sizes: '180x180',
            href: withBase('apple-touch-icon.png?v=1'),
          },
        ],
        ['link', { rel: 'manifest', href: withBase('site.webmanifest?v=1') }],

        ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
        ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
        [
          'link',
          {
            rel: 'stylesheet',
            href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap',
          },
        ],

        ['meta', { name: 'author', content: AUTHOR }],
        ['meta', { name: 'theme-color', content: '#3eaf7c' }],
        ['meta', { name: 'viewport', content: 'width=device-width,initial-scale=1' }],
        ['meta', { property: 'og:type', content: 'website' }],
        ['meta', { property: 'og:site_name', content: SITE_NAME }],
        ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
      ],

      pwa: {
        registerType: 'autoUpdate',
        workbox: {
          cleanupOutdatedCaches: true,
          clientsClaim: true,
          skipWaiting: true,
        },
      },

      cleanUrls: true,
      srcDir: '.',
      srcExclude: ['**/README.md', '**/TODO.md', '**/node_modules/**', '**/.vitepress/**'],
      outDir: './.vitepress/dist',
      cacheDir: './.vitepress/cache',
      assetsDir: 'assets',

      ignoreDeadLinks: [/^https?:\/\/localhost/, '/playground', /^https?:\/\/twitter\.com/],

      appearance: true,
      lastUpdated: true,

      sitemap: { hostname: SITE_URL },

      markdown: {
        headers: { level: [2, 3, 4] },
        theme: { light: 'github-light', dark: 'github-dark' },
        lineNumbers: true,
        anchor: { permalink: true },
        toc: { level: [2, 3] },
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
        image: { lazyLoading: true },
        highlightLines: true,
        attrs: { leftDelimiter: '{', rightDelimiter: '}' },
      },

      vite: {
        server: { port: 5173, host: true },
        build: { chunkSizeWarningLimit: 1500 },
        ssr: { noExternal: ['vitepress-plugin-pagefind'] },
        plugins: [
          pagefindPlugin({
            btnPlaceholder: 'Search',
            placeholder: 'Search documentation...',
            emptyText: 'No results found',
            heading: 'Total: {{searchResult}} results',
            excludeSelector: ['img', 'a.header-anchor', '.vp-doc'],
            forceLanguage: 'en',
            showEmpty: false,
            indexing: { start: 'docs', glob: '**/*.{md,html}' },
          }),
          llmstxt({ generateLLMsTxt: true, generateLLMsFullTxt: true }),
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
          { text: 'Home', link: '/' },
          { text: 'Courses', link: '/v1/courses/' },
          { text: 'Information', link: '/v1/information/' },
          { text: 'Tasks', link: '/v1/task/' },
          { text: 'Format', link: '/format' },
          { text: 'License', link: '/license' }, // ← tambah ini
          { text: 'About', link: '/v1/about' },
          {
            text: 'Version',
            items: VERSIONS.map((v) => ({
              text: v.badge ? `${v.label} (${v.badge})` : v.label,
              link: v.link,
            })),
          },
        ],

        sidebar,

        socialLinks: [{ icon: 'github', link: REPO_URL }],

        footer: {
          message:
            'Released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener">CC BY-NC-SA 4.0</a> License.',
          copyright: `Copyright © 2026-present ${AUTHOR}`,
        },

        editLink: {
          pattern: `${REPO_URL}/edit/master/docs/:path`,
          text: 'Edit this page on GitHub',
        },

        lastUpdated: {
          text: 'Last updated',
          formatOptions: { dateStyle: 'short', timeStyle: 'medium', forceLocale: true },
        },

        search: {
          provider: 'local',
          options: {
            translations: {
              button: { buttonText: 'Search', buttonAriaLabel: 'Search' },
              modal: {
                displayDetails: 'Display detailed list',
                resetButtonTitle: 'Reset search',
                backButtonTitle: 'Close search',
                noResultsText: 'No results found',
                footer: {
                  selectText: 'Select',
                  selectKeyAriaLabel: 'Enter',
                  navigateText: 'Navigate',
                  navigateUpKeyAriaLabel: 'Up arrow',
                  navigateDownKeyAriaLabel: 'Down arrow',
                  closeText: 'Close',
                  closeKeyAriaLabel: 'Escape',
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

        docFooter: { prev: 'Previous', next: 'Next' },
        outline: { level: [2, 3], label: 'On this page' },

        darkModeSwitchLabel: 'Appearance',
        lightModeSwitchTitle: 'Switch to light theme',
        darkModeSwitchTitle: 'Switch to dark theme',

        sidebarMenuLabel: 'Menu',
        returnToTopLabel: 'Return to top',
        langMenuLabel: 'Change language',
        externalLinkIcon: true,

        notFound: {
          title: 'Page Not Found',
          quote:
            "But if you don't change direction, and continue to search, you may end up where you are headed.",
          linkLabel: 'go to home',
          linkText: 'Take me home',
        },
      },
    })
  )
);
