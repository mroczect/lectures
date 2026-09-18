import type * as Preset from '@docusaurus/preset-classic';

const REPO_URL = 'https://github.com/mroczect/lectures';

export const footer: Preset.ThemeConfig['footer'] = {
    style: 'dark',
    links: [
        {
            title: 'Dokumentasi',
            items: [
                { label: 'Pengantar', to: '/docs/intro' },
                { label: 'Format & Aturan', to: '/docs/format/page' },
                { label: 'Lisensi', to: '/docs/license' },
            ],
        },
        {
            title: 'Versi 1',
            items: [
                { label: 'Beranda v1', to: '/docs/v1/' },
                { label: 'Mata Kuliah', to: '/docs/v1/courses/' },
                { label: 'Informasi', to: '/docs/v1/information/' },
                { label: 'Tugas', to: '/docs/v1/task/' },
            ],
        },
        {
            title: 'Lainnya',
            items: [
                { label: 'Blog', to: '/blog' },
                { label: 'GitHub', href: REPO_URL },
            ],
        },
    ],
    copyright: `Copyright © ${new Date().getFullYear()} Muhammad Riduwan Khafidi · CC BY-NC-SA 4.0`,
};
