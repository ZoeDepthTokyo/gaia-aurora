import { CSSProperties, ReactNode } from 'react';
import { LucideIcon, TrendingUp, TrendingDown } from 'lucide-react';
import { Card } from '../molecules/Card';

export interface StatCardProps {
  icon: LucideIcon;
  label: string;
  value: string | number;
  change?: {
    value: number;
    type: 'increase' | 'decrease';
    label?: string;
  };
  color?: string;
  suffix?: string;
}

export const StatCard = ({
  icon: Icon,
  label,
  value,
  change,
  color = 'var(--js-primary)',
  suffix
}: StatCardProps) => {
  const headerStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 'var(--js-space-sm)'
  };

  const iconStyles: CSSProperties = {
    color: color
  };

  const valueStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-metric)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-metric)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    marginBottom: '4px',
    fontFamily: suffix ? 'var(--js-font-mono)' : 'inherit'
  };

  const labelStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    fontWeight: 'var(--js-font-weight-medium)',
    color: 'var(--js-text)',
    marginBottom: '4px'
  };

  const changeStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: change?.type === 'increase' ? 'var(--js-success)' : 'var(--js-text)',
    opacity: change?.type === 'decrease' ? 0.6 : 1,
    display: 'flex',
    alignItems: 'center',
    gap: 'var(--js-space-xs)'
  };

  const TrendIcon = change?.type === 'increase' ? TrendingUp : TrendingDown;

  return (
    <Card padding="default" elevation={1}>
      <div style={headerStyles}>
        <Icon size={20} style={iconStyles} />
        {change && (
          <TrendIcon
            size={16}
            style={{
              color: change.type === 'increase' ? 'var(--js-success)' : 'var(--js-text)',
              opacity: change.type === 'decrease' ? 0.6 : 1
            }}
          />
        )}
      </div>
      <div style={valueStyles}>
        {value}{suffix}
      </div>
      <div style={labelStyles}>{label}</div>
      {change && (
        <div style={changeStyles}>
          {change.label || `${change.type === 'increase' ? '+' : ''}${change.value}${suffix || ''}`}
        </div>
      )}
    </Card>
  );
};

export interface StatsGridProps {
  stats: StatCardProps[];
  columns?: 2 | 3 | 4;
}

export const StatsGrid = ({ stats, columns = 4 }: StatsGridProps) => {
  const gridStyles: CSSProperties = {
    display: 'grid',
    gridTemplateColumns: `repeat(auto-fit, minmax(200px, 1fr))`,
    gap: 'var(--js-space-md)'
  };

  return (
    <div style={gridStyles}>
      {stats.map((stat, index) => (
        <StatCard key={index} {...stat} />
      ))}
    </div>
  );
};
