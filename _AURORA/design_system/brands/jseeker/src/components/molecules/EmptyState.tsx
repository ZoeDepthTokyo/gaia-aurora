import { ReactNode, CSSProperties } from 'react';
import { LucideIcon } from 'lucide-react';
import { Button } from '../atoms/Button';

export interface EmptyStateProps {
  icon?: LucideIcon;
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
    icon?: ReactNode;
  };
  className?: string;
  style?: CSSProperties;
}

export const EmptyState = ({
  icon: Icon,
  title,
  description,
  action,
  className = '',
  style = {}
}: EmptyStateProps) => {
  const containerStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    padding: 'var(--js-space-xxl)',
    fontFamily: 'var(--js-font-system)',
    ...style
  };

  const iconWrapperStyles: CSSProperties = {
    width: '64px',
    height: '64px',
    borderRadius: 'var(--js-border-radius-full)',
    backgroundColor: 'var(--js-surface)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 'var(--js-space-lg)',
    color: 'var(--js-text)',
    opacity: 0.4
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h3)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    margin: '0 0 8px 0'
  };

  const descriptionStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    opacity: 0.6,
    maxWidth: '480px',
    margin: '0 0 var(--js-space-lg) 0'
  };

  return (
    <div style={containerStyles} className={className}>
      {Icon && (
        <div style={iconWrapperStyles}>
          <Icon size={32} />
        </div>
      )}
      <h3 style={titleStyles}>{title}</h3>
      {description && <p style={descriptionStyles}>{description}</p>}
      {action && (
        <Button
          variant="primary"
          onClick={action.onClick}
          iconLeft={action.icon}
        >
          {action.label}
        </Button>
      )}
    </div>
  );
};
