import type * as Preset from '@docusaurus/preset-classic';

export const metadata: Preset.ThemeConfig['metadata'] = [
    { name: 'author', content: 'Muhammad Riduwan Khafidi' },
    { name: 'theme-color', content: '#000000' },
    {
        name: 'description',
        content:
            'Dokumentasi materi kuliah, tugas, dan catatan untuk mahasiswa Teknologi Rekayasa Perangkat Lunak Politeknik Negeri Batam.',
    },
    { property: 'og:type', content: 'website' },
    { property: 'og:title', content: 'Lectures — Dokumentasi Kuliah TRPL Polibatam' },
    {
        property: 'og:description',
        content: 'Satu proyek, semua sumber — materi, jadwal, tugas, dan referensi akademik.',
    },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: 'Lectures — Dokumentasi Kuliah TRPL Polibatam' },
];
