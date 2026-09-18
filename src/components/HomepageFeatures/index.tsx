import type { ReactNode, MouseEvent } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type Span = 'narrow' | 'wide';

type FeatureItem = {
	title: string;
	Svg: React.ComponentType<React.ComponentProps<'svg'>>;
	description: ReactNode;
	span?: Span;
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

function CourseIcon(props: React.ComponentProps<'svg'>) {
	return (
		<svg {...iconProps} {...props}>
			<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
			<path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
		</svg>
	);
}
function InfoIcon(props: React.ComponentProps<'svg'>) {
	return (
		<svg {...iconProps} {...props}>
			<circle cx="12" cy="12" r="10" />
			<line x1="12" y1="16" x2="12" y2="12" />
			<line x1="12" y1="8" x2="12.01" y2="8" />
		</svg>
	);
}
function TaskIcon(props: React.ComponentProps<'svg'>) {
	return (
		<svg {...iconProps} {...props}>
			<path d="M9 11l3 3L22 4" />
			<path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11" />
		</svg>
	);
}
function VersionIcon(props: React.ComponentProps<'svg'>) {
	return (
		<svg {...iconProps} {...props}>
			<circle cx="12" cy="12" r="10" />
			<polyline points="12 6 12 12 16 14" />
		</svg>
	);
}
function SearchIcon(props: React.ComponentProps<'svg'>) {
	return (
		<svg {...iconProps} {...props}>
			<circle cx="11" cy="11" r="8" />
			<line x1="21" y1="21" x2="16.65" y2="16.65" />
		</svg>
	);
}
function OpenIcon(props: React.ComponentProps<'svg'>) {
	return (
		<svg {...iconProps} {...props}>
			<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22" />
		</svg>
	);
}

const FeatureList: FeatureItem[] = [
	{
		title: 'Materi Kuliah',
		Svg: CourseIcon,
		span: 'wide',
		description:
			'Catatan kuliah, daftar bacaan, dan materi referensi yang tersusun per semester untuk setiap mata kuliah dalam kurikulum.',
	},
	{
		title: 'Informasi Akademik',
		Svg: InfoIcon,
		span: 'narrow',
		description:
			'Jadwal kelas, kontak dosen, dan pembagian tim Project-Based Learning dalam satu tempat.',
	},
	{
		title: 'Tugas',
		Svg: TaskIcon,
		span: 'narrow',
		description:
			'Brief tugas, persyaratan pengumpulan, dan sumber pendukung yang diorganisir per mata kuliah.',
	},
	{
		title: 'Konten Berversi',
		Svg: VersionIcon,
		span: 'wide',
		description:
			'Setiap periode akademik tersimpan pada jalur versinya sendiri sehingga materi sebelumnya tetap dapat diakses dan dikutip.',
	},
	{
		title: 'Pencarian',
		Svg: SearchIcon,
		span: 'narrow',
		description:
			'Pencarian teks lengkap di seluruh dokumentasi, dengan filter mata kuliah, topik, dan versi.',
	},
	{
		title: 'Sumber Terbuka',
		Svg: OpenIcon,
		span: 'narrow',
		description:
			'Seluruh konten tersedia publik di bawah Lisensi MIT dan terbuka untuk kontribusi mahasiswa maupun dosen.',
	},
];

function Feature({ title, Svg, description, span = 'narrow' }: FeatureItem) {
	const handleMouseMove = (e: MouseEvent<HTMLElement>) => {
		const rect = e.currentTarget.getBoundingClientRect();
		e.currentTarget.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
		e.currentTarget.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
	};

	return (
		<div className={clsx('col', span === 'wide' ? 'col--8' : 'col--4', 'col--6')}>
			<article className={styles.featureCard} onMouseMove={handleMouseMove}>
				<div className={styles.featureIcon}>
					<Svg className={styles.featureSvg} />
				</div>
				<div className={styles.featureContent}>
					<Heading as="h3" className={styles.featureTitle}>
						{title}
					</Heading>
					<p className={styles.featureDescription}>{description}</p>
				</div>
			</article>
		</div>
	);
}

export default function HomepageFeatures(): ReactNode {
	return (
		<section className={styles.features}>
			<div className="container">
				<div className={styles.sectionHeader}>
					<span className={styles.sectionEyebrow}>Fitur</span>
					<h2 className={styles.sectionTitle}>Segala hal yang kamu butuhkan.</h2>
					<p className={styles.sectionSubtitle}>
						Dari catatan kuliah hingga pencarian teks lengkap — semua terorganisir dalam
						satu tempat.
					</p>
				</div>
				<div className="row">
					{FeatureList.map((props) => (
						<Feature key={props.title} {...props} />
					))}
				</div>
			</div>
		</section>
	);
}
