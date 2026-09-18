import type * as Preset from '@docusaurus/preset-classic';
import { navbar } from './navbar';
import { footer } from './footer';
import { prism } from './prism';
import { metadata } from './metadata';

export const themeConfig: Preset.ThemeConfig = {
    image: 'img/docusaurus-social-card.jpg',
    metadata,
    navbar,
    footer,
    prism,

    colorMode: {
        defaultMode: 'dark',
        disableSwitch: true,
        respectPrefersColorScheme: false,
    },

    docs: {
        sidebar: {
            hideable: true,
            autoCollapseCategories: false,
        },
    },

    tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 4,
    },
};
