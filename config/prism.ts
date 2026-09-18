import { themes as prismThemes } from 'prism-react-renderer';
import type * as Preset from '@docusaurus/preset-classic';

export const prism: Preset.ThemeConfig['prism'] = {
    theme: prismThemes.github,
    darkTheme: prismThemes.dracula,
    additionalLanguages: ['bash', 'json', 'typescript', 'python', 'sql', 'java', 'yaml'],
};
