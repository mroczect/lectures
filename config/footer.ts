import type * as Preset from '@docusaurus/preset-classic';

const REPO_URL = 'https://github.com/mroczect/lectures';

export const footer: Preset.ThemeConfig['footer'] = {
  style: 'dark',
  links: [
    {
      title: 'Docs',
      items: [{label: 'Tutorial', to: '/docs/intro'}],
    },
    {
      title: 'Community',
      items: [
        {
          label: 'Stack Overflow',
          href: 'https://stackoverflow.com/questions/tagged/docusaurus',
        },
        {
          label: 'Discord',
          href: 'https://discordapp.com/invite/docusaurus',
        },
        {
          label: 'X',
          href: 'https://x.com/docusaurus',
        },
      ],
    },
    {
      title: 'More',
      items: [
        {label: 'Blog', to: '/blog'},
        {label: 'GitHub', href: REPO_URL},
      ],
    },
  ],
  copyright: `Copyright © ${new Date().getFullYear()} Muhammad Riduwan Khafidi.`,
};
