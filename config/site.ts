import type { Config } from '@docusaurus/types';

type SiteConfig = Omit<Config, 'i18n' | 'presets' | 'themeConfig'>;

export const site: SiteConfig = {
    title: 'Lectures',
    tagline: 'Dokumentasi materi kuliah, tugas, dan catatan',
    favicon: 'img/favicon.ico',
    url: 'https://mroczect.github.io',
    baseUrl: '/lectures/',
    organizationName: 'mroczect',
    projectName: 'lectures',
    deploymentBranch: 'gh-pages',
    trailingSlash: false,
    onBrokenLinks: 'throw',
    future: {
        v4: true,
    },
    headTags: [
        {
            tagName: 'link',
            attributes: { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        },
        {
            tagName: 'link',
            attributes: {
                rel: 'preconnect',
                href: 'https://fonts.gstatic.com',
                crossorigin: 'true',
            },
        },
    ],
    markdown: {
        mermaid: true,
        hooks: {
            onBrokenMarkdownLinks: 'warn',
        },
    },
};
