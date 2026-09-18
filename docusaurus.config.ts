import type { Config } from '@docusaurus/types';
import { site, i18n, presets, themes, plugins, themeConfig } from './config';

const config: Config = {
    ...site,
    i18n,
    presets,
    themes,
    plugins,
    themeConfig,
};

export default config;
