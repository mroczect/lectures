import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type IconKey = 'book' | 'clipboard' | 'check' | 'tag' | 'file' | 'globe';

type FeatureItem = {
    title: string;
    description: string;
    icon: IconKey;
    link: string;
};

const iconProps = {
    width: 20,
    height: 20,
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: 1.75,
    strokeLinecap: 'round' as const,
    strokeLinejoin: 'round' as const,
    'aria-hidden': true,
};

const icons: Record<IconKey, ReactNode> = {
    book: (
        <svg {...iconProps}>
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
    ),
    clipboard: (
        <svg {...iconProps}>
            <rect x="8" y="2" width="8" height="4" rx="1" />
            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" />
            <path d="M9 12h6M9 16h4" />
        </svg>
    ),
    check: (
        <svg {...iconProps}>
            <path d="M9 11l3 3L22 4" />
            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11" />
        </svg>
    ),
    tag: (
        <svg {...iconProps}>
            <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z" />
            <circle cx="7" cy="7" r="1.5" />
        </svg>
    ),
    file: (
        <svg {...iconProps}>
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
            <polyline points="14 2 14 8 20 8" />
            <path d="M9 13h6M9 17h4" />
        </svg>
    ),
    globe: (
        <svg {...iconProps}>
            <circle cx="12" cy="12" r="10" />
            <path d="M2 12h20" />
            <path d="M12 2a15 15 0 0 1 4 10 15 15 0 0 1-4 10 15 15 0 0 1-4-10 15 15 0 0 1 4-10z" />
        </svg>
    ),
};

const FeatureList: FeatureItem[] = [
    {
        title: 'Materi Kuliah',
        description: 'Catatan, bacaan, dan referensi per mata kuliah, tersusun per semester.',
        icon: 'book',
        link: '/docs/v1/courses/',
    },
    {
        title: 'Informasi Akademik',
        description: 'Jadwal kelas, kontak dosen, dan data tim PBL dalam satu tempat.',
        icon: 'clipboard',
        link: '/docs/v1/information/',
    },
    {
        title: 'Tugas',
        description: 'Daftar tugas, syarat pengumpulan, dan sumber pendukung per mata kuliah.',
        icon: 'check',
        link: '/docs/v1/task/',
    },
    {
        title: 'Konten Berversi',
        description: 'Tiap semester punya jalur versinya sendiri — materi lama tetap bisa diakses.',
        icon: 'tag',
        link: '/docs/v1/',
    },
    {
        title: 'Format & Aturan',
        description: 'Konvensi penulisan, penamaan file, dan panduan kontribusi.',
        icon: 'file',
        link: '/docs/format/page',
    },
    {
        title: 'Sumber Terbuka',
        description: 'Diterbitkan dengan lisensi CC BY-NC-SA 4.0 untuk penggunaan non-komersial.',
        icon: 'globe',
        link: '/docs/license',
    },
];

function Feature({ title, description, icon, link }: FeatureItem) {
    return (
        <div className={clsx('col col--4')}>
            <Link to={link} className={styles.featureCard}>
                <span className={styles.featureIcon}>{icons[icon]}</span>
                <Heading as="h3" className={styles.featureTitle}>
                    {title}
                </Heading>
                <p className={styles.featureDescription}>{description}</p>
                <span className={styles.featureArrow} aria-hidden="true">
                    →
                </span>
            </Link>
        </div>
    );
}

export default function HomepageFeatures(): ReactNode {
    return (
        <section className={styles.features}>
            <div className="container">
                <div className="row">
                    {FeatureList.map((item, idx) => (
                        <Feature key={idx} {...item} />
                    ))}
                </div>
            </div>
        </section>
    );
}
