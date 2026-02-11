import { ReactNode, CSSProperties } from 'react';
import { ArrowLeft } from 'lucide-react';
import { Button } from '../atoms/Button';
import { Card } from '../molecules/Card';

export interface DetailViewTemplateProps {
  title: string;
  subtitle?: string;
  backLabel?: string;
  onBack?: () => void;
  headerActions?: ReactNode;
  metadata?: Array<{
    label: string;
    value: ReactNode;
  }>;
  sidebar?: ReactNode;
  children: ReactNode;
  footer?: ReactNode;
}

export const DetailViewTemplate = ({
  title,
  subtitle,
  backLabel = 'Back',
  onBack,
  headerActions,
  metadata,
  sidebar,
  children,
  footer
}: DetailViewTemplateProps) => {
  const containerStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-xl)',
    fontFamily: 'var(--js-font-system)'
  };

  const backButtonStyles: CSSProperties = {
    marginBottom: 'var(--js-space-md)'
  };

  const headerStyles: CSSProperties = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    gap: 'var(--js-space-lg)',
    paddingBottom: 'var(--js-space-lg)',
    borderBottom: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const headerContentStyles: CSSProperties = {
    flex: 1
  };

  const titleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-h1)',
    fontWeight: 'var(--js-font-weight-semibold)',
    lineHeight: 'var(--js-line-height-h1)',
    letterSpacing: 'var(--js-letter-spacing-display)',
    color: 'var(--js-text)',
    margin: '0 0 8px 0'
  };

  const subtitleStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body-l)',
    lineHeight: 'var(--js-line-height-body-l)',
    color: 'var(--js-text)',
    opacity: 0.7,
    margin: 0
  };

  const metadataStyles: CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: 'var(--js-space-lg)',
    padding: 'var(--js-space-lg)',
    backgroundColor: 'var(--js-surface)',
    borderRadius: 'var(--js-border-radius-md)',
    border: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const metadataItemStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-xs)'
  };

  const metadataLabelStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-caption)',
    lineHeight: 'var(--js-line-height-caption)',
    fontWeight: 'var(--js-font-weight-semibold)',
    textTransform: 'uppercase',
    letterSpacing: 'var(--js-letter-spacing-uppercase)',
    color: 'var(--js-text)',
    opacity: 0.6
  };

  const metadataValueStyles: CSSProperties = {
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    fontWeight: 'var(--js-font-weight-semibold)',
    color: 'var(--js-text)'
  };

  const mainContentStyles: CSSProperties = {
    display: 'grid',
    gridTemplateColumns: sidebar ? '1fr 320px' : '1fr',
    gap: 'var(--js-space-xl)',
    alignItems: 'start'
  };

  const contentColumnStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-lg)'
  };

  const sidebarStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-md)',
    position: 'sticky',
    top: 'calc(var(--js-header-height) + var(--js-space-lg))'
  };

  return (
    <div style={containerStyles}>
      {/* Back Button */}
      {onBack && (
        <div style={backButtonStyles}>
          <Button
            variant="ghost"
            size="sm"
            iconLeft={<ArrowLeft size={16} />}
            onClick={onBack}
          >
            {backLabel}
          </Button>
        </div>
      )}

      {/* Header */}
      <div style={headerStyles}>
        <div style={headerContentStyles}>
          <h1 style={titleStyles}>{title}</h1>
          {subtitle && <p style={subtitleStyles}>{subtitle}</p>}
        </div>
        {headerActions && <div>{headerActions}</div>}
      </div>

      {/* Metadata */}
      {metadata && metadata.length > 0 && (
        <div style={metadataStyles}>
          {metadata.map((item, index) => (
            <div key={index} style={metadataItemStyles}>
              <span style={metadataLabelStyles}>{item.label}</span>
              <div style={metadataValueStyles}>{item.value}</div>
            </div>
          ))}
        </div>
      )}

      {/* Main Content with Optional Sidebar */}
      <div style={mainContentStyles}>
        <div style={contentColumnStyles}>
          {children}
        </div>
        {sidebar && (
          <aside style={sidebarStyles}>
            {sidebar}
          </aside>
        )}
      </div>

      {/* Footer */}
      {footer && (
        <div style={{
          paddingTop: 'var(--js-space-lg)',
          borderTop: `var(--js-border-width-thin) solid var(--js-border)`
        }}>
          {footer}
        </div>
      )}
    </div>
  );
};
