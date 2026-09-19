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
            <div className="container">
                <Heading as="h1" className="hero__title">
                    Lectures
                </Heading>
                <p className="hero__subtitle">Dokumentasi kuliah TRPL Politeknik Negeri Batam</p>
                <div className={styles.buttons}>
                    <Link className="button button--secondary button--lg" to="/docs/v1/">
                        Buka dokumentasi
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

function QuickLinks() {
    const links = [
        { label: 'Mata Kuliah', to: '/docs/v1/courses/' },
        { label: 'Informasi Akademik', to: '/docs/v1/information/' },
        { label: 'Tugas', to: '/docs/v1/task/' },
        { label: 'Format & Aturan', to: '/docs/format/page' },
        { label: 'Lisensi', to: '/docs/license' },
        { label: 'Tentang', to: '/docs/v1/about' },
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
                            <Link to={l.to}>{l.label}</Link>
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
