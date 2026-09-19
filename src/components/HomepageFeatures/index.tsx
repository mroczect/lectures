import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
    title: string;
    description: string;
};

const FeatureList: FeatureItem[] = [
    {
        title: 'Materi Kuliah',
        description: 'Catatan, bacaan, dan referensi per mata kuliah, tersusun per semester.',
    },
    {
        title: 'Informasi Akademik',
        description: 'Jadwal kelas, kontak dosen, dan data tim PBL dalam satu tempat.',
    },
    {
        title: 'Tugas',
        description: 'Daftar tugas, syarat pengumpulan, dan sumber pendukung per mata kuliah.',
    },
    {
        title: 'Konten Berversi',
        description: 'Tiap semester punya jalur versinya sendiri — materi lama tetap bisa diakses.',
    },
    {
        title: 'Format & Aturan',
        description: 'Konvensi penulisan, penamaan file, dan panduan kontribusi.',
    },
    {
        title: 'Sumber Terbuka',
        description: 'Diterbitkan dengan lisensi CC BY-NC-SA 4.0 untuk penggunaan non-komersial.',
    },
];

function Feature({ title, description }: FeatureItem) {
    return (
        <div className={clsx('col col--4')}>
            <div className={styles.feature}>
                <Heading as="h3">{title}</Heading>
                <p>{description}</p>
            </div>
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
