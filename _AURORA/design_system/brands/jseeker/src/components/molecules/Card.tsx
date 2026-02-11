import { ReactNode, CSSProperties } from 'react';

export interface CardProps {
  children: ReactNode;
  padding?: 'compact' | 'default' | 'spacious';
  elevation?: 0 | 1 | 2 | 3 | 4;
  className?: string;
  style?: CSSProperties;
  onClick?: () => void;
  hoverable?: boolean;
}

export const Card = ({
  children,
  padding = 'default',
  elevation = 1,
  className = '',
  style = {},
  onClick,
  hoverable = false
}: CardProps) => {
  const paddingMap = {
    compact: 'var(--js-card-padding-compact)',
    default: 'var(--js-card-padding-default)',
    spacious: 'var(--js-card-padding-spacious)'
  };

  const shadowMap = {
    0: 'var(--js-shadow-0)',
    1: 'var(--js-shadow-1)',
    2: 'var(--js-shadow-2)',
    3: 'var(--js-shadow-3)',
    4: 'var(--js-shadow-4)'
  };

  const cardStyles: CSSProperties = {
    backgroundColor: 'var(--js-surface)',
    border: `var(--js-border-width-thin) solid var(--js-border)`,
    borderRadius: 'var(--js-border-radius-md)',
    padding: paddingMap[padding],
    boxShadow: shadowMap[elevation],
    fontFamily: 'var(--js-font-system)',
    transition: hoverable ? 'all 200ms cubic-bezier(0.4, 0, 0.2, 1)' : 'none',
    cursor: onClick ? 'pointer' : 'default',
    ...style
  };

  const handleMouseEnter = (e: React.MouseEvent<HTMLDivElement>) => {
    if (hoverable && elevation < 4) {
      e.currentTarget.style.boxShadow = shadowMap[Math.min(elevation + 1, 4) as 0 | 1 | 2 | 3 | 4];
      e.currentTarget.style.transform = 'translateY(-2px)';
    }
  };

  const handleMouseLeave = (e: React.MouseEvent<HTMLDivElement>) => {
    if (hoverable) {
      e.currentTarget.style.boxShadow = shadowMap[elevation];
      e.currentTarget.style.transform = 'translateY(0)';
    }
  };

  return (
    <div
      style={cardStyles}
      className={className}
      onClick={onClick}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {children}
    </div>
  );
};

export interface CardHeaderProps {
  title: string;
  subtitle?: string;
  action?: ReactNode;
}

export const CardHeader = ({ title, subtitle, action }: CardHeaderProps) => {
  const headerStyles: CSSProperties = {
    display: 'flex',
    alignItems: 'flex-start',
    justifyContent: 'space-between',
    gap: 'var(--js-space-md)',
    marginBottom: 'var(--js-space-md)'
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h3)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h3)',
    letterSpacing: 'var(--js-letter-spacing-tight)',
    color: 'var(--js-text)',
    margin: 0
  };

  const subtitleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    color: 'var(--js-text)',
    opacity: 0.6,
    marginTop: '4px'
  };

  return (
    <div style={headerStyles}>
      <div>
        <h3 style={titleStyles}>{title}</h3>
        {subtitle && <p style={subtitleStyles}>{subtitle}</p>}
      </div>
      {action && <div>{action}</div>}
    </div>
  );
};

export interface CardContentProps {
  children: ReactNode;
}

export const CardContent = ({ children }: CardContentProps) => {
  return <div>{children}</div>;
};
