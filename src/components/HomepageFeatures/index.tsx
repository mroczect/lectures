import type { ReactNode, MouseEvent } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type IconKey = 'course' | 'info' | 'task' | 'version' | 'search' | 'format' | 'open';

export type FeatureItem = {
    icon?: IconKey;
    title: string;
    description: string;
    link?: string;
    linkText?: string;
    span?: 'narrow' | 'wide';
};

export type HomepageFeaturesProps = {
    eyebrow?: string;
    title: string;
    subtitle?: string;
    items: FeatureItem[];
};

const iconProps: React.SVGProps<SVGSVGElement> = {
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    strokeWidth: 1.5,
    strokeLinecap: 'round',
    strokeLinejoin: 'round',
    'aria-hidden': 'true',
};

const icons: Record<IconKey, (props: React.ComponentProps<'svg'>) => ReactNode> = {
    course: (props) => (
        <svg {...iconProps} {...props}>
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
        </svg>
    ),
    info: (props) => (
        <svg {...iconProps} {...props}>
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="16" x2="12" y2="12" />
            <line x1="12" y1="8" x2="12.01" y2="8" />
        </svg>
    ),
    task: (props) => (
        <svg {...iconProps} {...props}>
            <path d="M9 11l3 3L22 4" />
            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11" />
        </svg>
    ),
    version: (props) => (
        <svg {...iconProps} {...props}>
            <circle cx="12" cy="12" r="10" />
            <polyline points="12 6 12 12 16 14" />
        </svg>
    ),
    search: (props) => (
        <svg {...iconProps} {...props}>
            <circle cx="11" cy="11" r="8" />
            <line x1="21" y1="21" x2="16.65" y2="16.65" />
        </svg>
    ),
    format: (props) => (
        <svg {...iconProps} {...props}>
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
            <polyline points="14 2 14 8 20 8" />
            <line x1="9" y1="13" x2="15" y2="13" />
            <line x1="9" y1="17" x2="13" y2="17" />
        </svg>
    ),
    open: (props) => (
        <svg {...iconProps} {...props}>
            <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" />
        </svg>
    ),
};

function Feature({
    icon = 'course',
    title,
    description,
    link,
    linkText,
    span = 'narrow',
}: FeatureItem) {
    const Icon = icons[icon];

    const handleMouseMove = (e: MouseEvent<HTMLElement>) => {
        const card = e.currentTarget;
        const rect = card.getBoundingClientRect();

        requestAnimationFrame(() => {
            card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
            card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
        });
    };

    return (
        <div className={clsx('col', span === 'wide' ? 'col--8' : 'col--4', 'col--6')}>
            <article className={styles.featureCard} onMouseMove={handleMouseMove}>
                <div className={styles.featureCardSpotlight} aria-hidden="true" />
                <div className={styles.featureIcon}>
                    <Icon className={styles.featureSvg} />
                </div>
                <div className={styles.featureContent}>
                    <Heading as="h3" className={styles.featureTitle}>
                        {title}
                    </Heading>
                    <p className={styles.featureDescription}>{description}</p>
                    {link && linkText && (
                        <Link to={link} className={styles.featureLink}>
                            {linkText}
                            <span aria-hidden="true" className={styles.featureLinkArrow}>
                                →
                            </span>
                        </Link>
                    )}
                </div>
            </article>
        </div>
    );
}

export default function HomepageFeatures({
    eyebrow,
    title,
    subtitle,
    items,
}: HomepageFeaturesProps): ReactNode {
    return (
        <section className={styles.features}>
            <div className="container">
                <div className={styles.sectionHeader}>
                    {eyebrow && <span className={styles.sectionEyebrow}>{eyebrow}</span>}
                    <h2 className={styles.sectionTitle}>{title}</h2>
                    {subtitle && <p className={styles.sectionSubtitle}>{subtitle}</p>}
                </div>
                <div className="row">
                    {items.map((item) => (
                        <Feature key={item.title} {...item} />
                    ))}
                </div>
            </div>
        </section>
    );
}
