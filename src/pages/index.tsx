import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
	const { siteConfig } = useDocusaurusContext();
	return (
		<header className={clsx('hero', styles.heroBanner)}>
			<div className="container">
				<span className={styles.heroBadge}>
					<span className={styles.heroBadgeDot} />
					Open Source · MIT License
				</span>

				<Heading as="h1" className={styles.heroTitle}>
					<span className={styles.heroTitleAccent}>{siteConfig.title}</span>
				</Heading>

				<p className={styles.heroSubtitle}>{siteConfig.tagline}</p>

				<div className={styles.buttons}>
					<Link className="button button--primary button--lg" to="/docs/intro">
						Mulai Membaca
					</Link>
					<Link className="button button--secondary button--lg" to="/blog">
						Blog
					</Link>
				</div>

				<div className={styles.preview} aria-hidden="true">
					<div className={styles.previewBar}>
						<span className={styles.previewDot} />
						<span className={styles.previewDot} />
						<span className={styles.previewDot} />
						<span className={styles.previewTitle}>snapcat — docs</span>
					</div>
					<pre className={styles.previewBody}>
						<span className={styles.previewPrompt}>$</span>
						<span className={styles.previewCmd}>snapcat open if2211</span>
						{'\n'}
						<span className={styles.previewComment}>
							# membuka catatan mata kuliah semester ini…
						</span>
						{'\n'}
						<span className={styles.previewArrow}>→</span>
						<span className={styles.previewPath}>/docs/if2211/overview</span>
						{'\n'}
						<span className={styles.previewPrompt}>$</span>
						<span className={styles.previewCmd}>snapcat search "algoritma greedy"</span>
						<span className={styles.previewCursor} />
					</pre>
				</div>
			</div>
		</header>
	);
}

export default function Home(): ReactNode {
	const { siteConfig } = useDocusaurusContext();
	return (
		<Layout title={siteConfig.title} description={siteConfig.tagline}>
			<HomepageHeader />
			<main>
				<HomepageFeatures />
			</main>
		</Layout>
	);
}
