import type { Config } from '@docusaurus/types';

const REPO_URL = 'https://github.com/mroczect/lectures';

export const presets: Config['presets'] = [
    [
        'classic',
        {
            docs: {
                sidebarPath: './sidebars.ts',
                editUrl: `${REPO_URL}/tree/main/`,
                showLastUpdateTime: true,
                breadcrumbs: true,
            },
            blog: {
                showReadingTime: true,
                editUrl: `${REPO_URL}/tree/main/`,
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
