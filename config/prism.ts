import { themes as prismThemes } from 'prism-react-renderer';
import type * as Preset from '@docusaurus/preset-classic';

export const prism: Preset.ThemeConfig['prism'] = {
    theme: prismThemes.vsDark,
    darkTheme: prismThemes.vsDark,
    additionalLanguages: [
        'bash',
        'json',
        'typescript',
        'tsx',
        'jsx',
        'python',
        'sql',
        'java',
        'yaml',
        'markdown',
    ],
    magicComments: [
        {
            className: 'theme-code-block-highlighted-line',
            line: 'highlight-next-line',
            block: { start: 'highlight-start', end: 'highlight-end' },
        },
    ],
};
