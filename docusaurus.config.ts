import type { Config } from '@docusaurus/types';
import { site, i18n, presets, themeConfig } from './config';

const config: Config = {
    ...site,
    i18n,
    presets,
    themeConfig,
};

export default config;
