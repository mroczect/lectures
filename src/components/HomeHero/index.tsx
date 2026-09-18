import type { ReactNode } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

export type HeroAction = {
	label: string;
	href: string;
	variant?: 'primary' | 'secondary' | 'outline';
};

export type HomeHeroProps = {
	badge?: string;
	title: string;
	highlight?: string;
	tagline: string;
	actions?: HeroAction[];
	showPreview?: boolean;
};

export default function HomeHero({
	badge,
	title,
	highlight,
	tagline,
	actions = [],
	showPreview = true,
}: HomeHeroProps): ReactNode {
	return (
		<header className={styles.hero}>
			<div className={styles.heroGrid} aria-hidden="true" />
			<div className={styles.heroGlow} aria-hidden="true" />
			<div className={styles.heroOrb} aria-hidden="true" />

			<div className={styles.heroInner}>
				{badge && (
					<Link to="/docs/v1/" className={styles.heroBadge}>
						<span className={styles.heroBadgeDot} />
						{badge}
						<svg
							className={styles.heroBadgeArrow}
							width="12"
							height="12"
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							strokeWidth="2"
							strokeLinecap="round"
							strokeLinejoin="round"
						>
							<path d="M5 12h14"></path>
							<path d="m12 5 7 7-7 7"></path>
						</svg>
					</Link>
				)}

				<h1 className={styles.heroTitle}>
					{title}
					<br />
					<span className={styles.heroHighlight}>{highlight}</span>
				</h1>

				<p className={styles.heroTagline}>{tagline}</p>

				{actions.length > 0 && (
					<div className={styles.heroActions}>
						{actions.map((action) => (
							<Link
								key={`${action.href}-${action.label}`}
								to={action.href}
								className={clsx(
									'button',
									'button--lg',
									action.variant === 'primary' && 'button--primary',
									action.variant === 'secondary' && 'button--secondary',
									(!action.variant || action.variant === 'outline') &&
										'button--outline'
								)}
							>
								{action.label}
							</Link>
						))}
					</div>
				)}

				{showPreview && (
					<div className={styles.previewWrapper}>
						<div className={styles.previewGlow} aria-hidden="true" />
						<div className={styles.preview} aria-hidden="true">
							<div className={styles.previewBar}>
								<span className={clsx(styles.previewDot, styles.previewDotRed)} />
								<span
									className={clsx(styles.previewDot, styles.previewDotYellow)}
								/>
								<span className={clsx(styles.previewDot, styles.previewDotGreen)} />
								<span className={styles.previewTitle}>lectures — zsh</span>
								<div className={styles.previewSpacer} />
								<span className={styles.previewTag}>v1.0.0</span>
							</div>
							<pre className={styles.previewBody}>
								<span className={styles.previewPrompt}>$</span>
								<span className={styles.previewCmd}>lectures open rpl101</span>
								{'\n'}
								<span className={styles.previewComment}>
									# membuka materi Pengantar RPL…
								</span>
								{'\n'}
								<span className={styles.previewArrow}>→</span>
								<span className={styles.previewPath}>/docs/v1/courses/rpl101</span>
								{'\n'}
								<span className={styles.previewPrompt}>$</span>
								<span className={styles.previewCmd}>
									lectures search "metodologi agile"
								</span>
								<span className={styles.previewCursor} />
							</pre>
						</div>
					</div>
				)}
			</div>
		</header>
	);
}
