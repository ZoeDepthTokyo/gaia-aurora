import { ReactNode, CSSProperties } from 'react';
import { AlertCircle, CheckCircle, Info, XCircle, X } from 'lucide-react';

export type AlertVariant = 'info' | 'success' | 'warning' | 'error';

export interface AlertProps {
  variant?: AlertVariant;
  title?: string;
  children: ReactNode;
  dismissible?: boolean;
  onDismiss?: () => void;
  className?: string;
  style?: CSSProperties;
}

export const Alert = ({
  variant = 'info',
  title,
  children,
  dismissible = false,
  onDismiss,
  className = '',
  style = {}
}: AlertProps) => {
  const variantConfig = {
    info: {
      icon: Info,
      color: 'var(--js-info)',
      bg: 'rgba(59, 130, 246, 0.1)'
    },
    success: {
      icon: CheckCircle,
      color: 'var(--js-success)',
      bg: 'rgba(16, 185, 129, 0.1)'
    },
    warning: {
      icon: AlertCircle,
      color: 'var(--js-warning)',
      bg: 'rgba(245, 158, 11, 0.1)'
    },
    error: {
      icon: XCircle,
      color: 'var(--js-error)',
      bg: 'rgba(220, 38, 38, 0.1)'
    }
  };

  const config = variantConfig[variant];
  const Icon = config.icon;

  const alertStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'flex-start',
    gap: 'var(--js-space-md)',
    padding: 'var(--js-space-md)',
    backgroundColor: config.bg,
    border: `var(--js-border-width-thin) solid ${config.color}`,
    borderRadius: 'var(--js-border-radius-md)',
    fontFamily: 'var(--js-font-system)',
    ...style
  };

  const iconStyles: CSSProperties = {
    color: config.color,
    flexShrink: 0,
    marginTop: '2px'
  };

  const contentStyles: CSSProperties = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-xs)'
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    margin: 0
  };

  const messageStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    opacity: 0.8,
    margin: 0
  };

  const dismissButtonStyles: CSSProperties = {
    background: 'none',
    border: 'none',
    padding: 0,
    cursor: 'pointer',
    color: 'var(--js-text)',
    opacity: 0.5,
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    flexShrink: 0
  };

  return (
    <div style={alertStyles} className={className} role="alert">
      <Icon size={20} style={iconStyles} />
      <div style={contentStyles}>
        {title && <h4 style={titleStyles}>{title}</h4>}
        <div style={messageStyles}>{children}</div>
      </div>
      {dismissible && (
        <button
          onClick={onDismiss}
          style={dismissButtonStyles}
          aria-label="Dismiss alert"
        >
          <X size={20} />
        </button>
      )}
    </div>
  );
};
