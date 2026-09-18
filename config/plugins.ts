import type { Config } from '@docusaurus/types';

export const plugins: Config['plugins'] = [
    'docusaurus-plugin-image-zoom',
    [
        'docusaurus-search-local',
        {
            hashed: true,
            indexDocs: true,
            indexPages: true,
            docsRouteBasePath: ['/docs'],
        },
    ],
];
