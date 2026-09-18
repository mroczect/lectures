import type * as Preset from '@docusaurus/preset-classic';

const REPO_URL = 'https://github.com/mroczect/lectures';

export const navbar: Preset.ThemeConfig['navbar'] = {
    title: 'Lectures',
    logo: {
        alt: 'Lectures Logo',
        src: 'img/logo.svg',
    },
    hideOnScroll: false,
    items: [
        {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Docs',
        },
        {
            to: '/blog',
            label: 'Blog',
            position: 'left',
        },
        {
            href: REPO_URL,
            label: 'GitHub',
            position: 'right',
        },
    ],
};
