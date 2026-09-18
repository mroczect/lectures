import type { Config } from '@docusaurus/types';

const REPO_URL = 'https://github.com/mroczect/lectures';

export const presets: Config['presets'] = [
    [
        'classic',
        {
            docs: {
                sidebarPath: './sidebars.ts',
                editUrl: `${REPO_URL}/tree/master/`,
                showLastUpdateTime: true,
                breadcrumbs: true,
            },
            blog: {
                showReadingTime: true,
                editUrl: `${REPO_URL}/tree/master/`,
                feedOptions: {
                    type: ['rss', 'atom'],
                    xslt: true,
                },
                onInlineTags: 'warn',
                onInlineAuthors: 'warn',
                onUntruncatedBlogPosts: 'warn',
            },
            theme: {
                customCss: './src/css/custom.css',
            },
        },
    ],
];

export const themes: Config['themes'] = ['@docusaurus/theme-mermaid'];
