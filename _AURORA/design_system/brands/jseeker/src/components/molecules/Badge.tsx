import { ReactNode, CSSProperties } from 'react';

export type BadgeVariant =
  | 'default'
  | 'primary'
  | 'success'
  | 'warning'
  | 'error'
  | 'info'
  | 'resume-draft'
  | 'resume-generating'
  | 'resume-ready'
  | 'resume-error'
  | 'app-applied'
  | 'app-interviewing'
  | 'app-offered'
  | 'app-rejected'
  | 'app-withdrawn'
  | 'job-active'
  | 'job-saved'
  | 'job-closed'
  | 'job-archived';

export interface BadgeProps {
  children: ReactNode;
  variant?: BadgeVariant;
  dot?: boolean;
  className?: string;
  style?: CSSProperties;
}

export const Badge = ({
  children,
  variant = 'default',
  dot = false,
  className = '',
  style = {}
}: BadgeProps) => {
  const variantStyles: Record<BadgeVariant, { bg: string; color: string }> = {
    default: { bg: 'var(--js-border)', color: 'var(--js-text)' },
    primary: { bg: 'var(--js-primary)', color: 'var(--js-bg)' },
    success: { bg: 'var(--js-success)', color: 'var(--js-bg)' },
    warning: { bg: 'var(--js-warning)', color: 'var(--js-bg)' },
    error: { bg: 'var(--js-error)', color: 'var(--js-bg)' },
    info: { bg: 'var(--js-info)', color: 'var(--js-bg)' },
    'resume-draft': { bg: 'var(--js-resume-draft)', color: 'var(--js-bg)' },
    'resume-generating': { bg: 'var(--js-resume-generating)', color: 'var(--js-bg)' },
    'resume-ready': { bg: 'var(--js-resume-ready)', color: 'var(--js-bg)' },
    'resume-error': { bg: 'var(--js-resume-error)', color: 'var(--js-bg)' },
    'app-applied': { bg: 'var(--js-app-applied)', color: 'var(--js-bg)' },
    'app-interviewing': { bg: 'var(--js-app-interviewing)', color: 'var(--js-bg)' },
    'app-offered': { bg: 'var(--js-app-offered)', color: 'var(--js-bg)' },
    'app-rejected': { bg: 'var(--js-app-rejected)', color: 'var(--js-bg)' },
    'app-withdrawn': { bg: 'var(--js-app-withdrawn)', color: 'var(--js-bg)' },
    'job-active': { bg: 'var(--js-job-active)', color: 'var(--js-bg)' },
    'job-saved': { bg: 'var(--js-job-saved)', color: 'var(--js-bg)' },
    'job-closed': { bg: 'var(--js-job-closed)', color: 'var(--js-bg)' },
    'job-archived': { bg: 'var(--js-job-archived)', color: 'var(--js-bg)' }
  };

  const badgeStyles: CSSProperties = {
    display: 'inline-flex',
    alignItems: 'center',
    gap: dot ? 'var(--js-space-xs)' : '0',
    fontSize: 'var(--js-font-size-caption)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-caption)',
    letterSpacing: 'var(--js-letter-spacing-uppercase)',
    textTransform: 'uppercase',
    fontFamily: 'var(--js-font-system)',
    color: variantStyles[variant].color,
    backgroundColor: variantStyles[variant].bg,
    padding: '4px 8px',
    borderRadius: 'var(--js-border-radius-sm)',
    whiteSpace: 'nowrap',
    ...style
  };

  const dotStyles: CSSProperties = {
    width: '6px',
    height: '6px',
    borderRadius: 'var(--js-border-radius-full)',
    backgroundColor: 'currentColor'
  };

  return (
    <span style={badgeStyles} className={className}>
      {dot && <span style={dotStyles} />}
      {children}
    </span>
  );
};
