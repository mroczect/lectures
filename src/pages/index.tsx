import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
    return (
        <header className={clsx('hero hero--primary', styles.heroBanner)}>
            <div className={styles.heroGrid} aria-hidden="true" />
            <div className={clsx('container', styles.heroContainer)}>
                <span className={styles.heroBadge}>
                    <span className={styles.heroBadgeDot} />
                    Open Source · CC BY-NC-SA 4.0
                </span>
                <Heading as="h1" className={clsx('hero__title', styles.heroTitle)}>
                    Lectures
                </Heading>
                <p className={clsx('hero__subtitle', styles.heroSubtitle)}>
                    Materi, jadwal, tugas, dan referensi akademik untuk Program Studi Teknologi
                    Rekayasa Perangkat Lunak, Politeknik Negeri Batam.
                </p>
                <div className={styles.buttons}>
                    <Link className="button button--secondary button--lg" to="/docs/v1/">
                        Buka dokumentasi
                    </Link>
                    <Link className="button button--outline button--lg" to="/docs/format/page">
                        Panduan format
                    </Link>
                    <Link
                        className="button button--outline button--lg"
                        href="https://github.com/mroczect/lectures"
                    >
                        GitHub
                    </Link>
                </div>
            </div>
        </header>
    );
}

type QuickLink = {
    label: string;
    description: string;
    to: string;
};

function QuickLinks() {
    const links: QuickLink[] = [
        {
            label: 'Mata Kuliah',
            description: 'Daftar 7 mata kuliah semester ini',
            to: '/docs/v1/courses/',
        },
        {
            label: 'Informasi Akademik',
            description: 'Jadwal, kontak dosen, tim PBL',
            to: '/docs/v1/information/',
        },
        {
            label: 'Tugas',
            description: 'Daftar tugas dan pengumpulan',
            to: '/docs/v1/task/',
        },
        {
            label: 'Format & Aturan',
            description: 'Konvensi penulisan dan kontribusi',
            to: '/docs/format/page',
        },
        {
            label: 'Lisensi',
            description: 'Ketentuan CC BY-NC-SA 4.0',
            to: '/docs/license',
        },
        {
            label: 'Tentang',
            description: 'Pengelola dokumentasi',
            to: '/docs/v1/about',
        },
    ];

    return (
        <section className={styles.quickLinks}>
            <div className="container">
                <Heading as="h2" className={styles.sectionTitle}>
                    Mulai dari sini
                </Heading>
                <ul className={styles.linkList}>
                    {links.map((l) => (
                        <li key={l.to}>
                            <Link to={l.to} className={styles.linkCard}>
                                <div className={styles.linkContent}>
                                    <span className={styles.linkLabel}>{l.label}</span>
                                    <span className={styles.linkDescription}>{l.description}</span>
                                </div>
                                <span className={styles.linkArrow} aria-hidden="true">
                                    →
                                </span>
                            </Link>
                        </li>
                    ))}
                </ul>
            </div>
        </section>
    );
}

export default function Home(): ReactNode {
    return (
        <Layout title="Lectures" description="Dokumentasi kuliah TRPL Politeknik Negeri Batam.">
            <HomepageHeader />
            <main>
                <HomepageFeatures />
                <QuickLinks />
            </main>
        </Layout>
    );
}
