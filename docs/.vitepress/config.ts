import { defineConfig } from 'vitepress';
import { generateSidebar } from 'vitepress-sidebar';
import { pagefindPlugin } from 'vitepress-plugin-pagefind';
import { withMermaid } from 'vitepress-mermaid-plugin';
import { withPwa } from '@vite-pwa/vitepress';
import { llmstxt } from 'vitepress-plugin-llms';
import { createSitemap } from 'vitepress-plugin-sitemap';
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

const SITE_URL = 'https://mroczect.biz.id/lectures';
const SITE_NAME = 'Lectures';
const AUTHOR = 'Muhammad Riduwan Khafidi';
const REPO_URL = 'https://github.com/mroczect/lectures.git';

export default withPwa(
  withMermaid(
    defineConfig({
      lang: 'en-US',
      title: SITE_NAME,
      titleTemplate: ':title - Complete Documentation',
      description:
        'A comprehensive documentation site built with VitePress 2.0 — featuring Mermaid, PWA, i18n, Pagefind, OpenAPI, LLM, and much more.',

      head: [
        // Icons
        ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }],
        ['link', { rel: 'icon', type: 'image/png', href: '/favicon-32x32.png' }],
        ['link', { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' }],

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
        ['meta', { name: 'author', content: AUTHOR }],
        ['meta', { name: 'theme-color', content: '#3eaf7c' }],
        ['meta', { name: 'viewport', content: 'width=device-width,initial-scale=1' }],
        ['meta', { property: 'og:type', content: 'website' }],
        ['meta', { property: 'og:site_name', content: SITE_NAME }],
        ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
        ['link', { rel: 'manifest', href: '/manifest.webmanifest' }],
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
            btnPlaceholder: 'Search',
            placeholder: 'Search documentation...',
            emptyText: 'No results found',
            heading: 'Total: {{searchResult}} results',
            excludeSelector: ['img', 'a.header-anchor', '.vp-doc'],
            forceLanguage: 'en',
            showEmpty: false,
            indexing: {
              start: 'docs',
              glob: '**/*.{md,html}',
            },
          }),

          llmstxt({
            domain: SITE_URL,
            generateLLMsFullTxt: true,
            generateLLMsTxt: true,
          }),
        ],
      },

      async buildEnd() {
        await createSitemap({
          hostname: SITE_URL,
          exclude: ['/404', '/private'],
        });
        console.log('✅ Sitemap generated');
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
        logo: '/logo.svg',
        siteTitle: SITE_NAME,

        nav: [
          { text: 'Home', link: '/' },
          { text: 'Guide', link: '/guide/' },
          { text: 'Reference', link: '/reference/' },
          {
            text: 'Ecosystem',
            items: [
              { text: 'VitePress', link: 'https://vitepress.dev' },
              { text: 'Vue', link: 'https://vuejs.org' },
              { text: 'Vite', link: 'https://vitejs.dev' },
            ],
          },
          {
            text: 'v2.0.0-alpha',
            items: [
              {
                text: 'Changelog',
                link: 'https://github.com/vuejs/vitepress/blob/main/CHANGELOG.md',
              },
              {
                text: 'Contributing',
                link: 'https://github.com/vuejs/vitepress/blob/main/.github/contributing.md',
              },
            ],
          },
        ],

        sidebar: generateSidebar([
          {
            documentRootPath: '/docs',
            scanStartPath: 'guide',
            resolvePath: '/guide/',
            collapsed: false,
            capitalizeFirst: true,
            useTitleFromFrontmatter: true,
            useTitleFromFileHeading: true,
            useFolderTitleFromIndexFile: true,
            sortMenusByFrontmatterOrder: true,
            manualSortFileNameByPriority: ['what-is-vitepress.md', 'getting-started.md'],
          },
          {
            documentRootPath: '/docs',
            scanStartPath: 'reference',
            resolvePath: '/reference/',
            collapsed: false,
            capitalizeFirst: true,
          },
        ]),

        socialLinks: [
          { icon: 'github', link: REPO_URL },
          { icon: 'twitter', link: 'https://twitter.com/username' },
          { icon: 'discord', link: 'https://discord.gg/invite' },
          { icon: 'youtube', link: 'https://youtube.com/@username' },
        ],

        footer: {
          message: 'Released under the MIT License.',
          copyright: `Copyright © 2026-present ${AUTHOR}`,
        },

        editLink: {
          pattern: `${REPO_URL}/edit/main/docs/:path`,
          text: 'Edit this page on GitHub',
        },

        lastUpdated: {
          text: 'Last updated',
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
                buttonText: 'Search',
                buttonAriaLabel: 'Search',
              },
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

        docFooter: {
          prev: 'Previous',
          next: 'Next',
        },

        outline: {
          level: [2, 3],
          label: 'On this page',
        },

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
