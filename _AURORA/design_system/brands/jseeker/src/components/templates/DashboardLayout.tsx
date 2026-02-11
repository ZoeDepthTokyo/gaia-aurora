import { ReactNode, CSSProperties, useState } from 'react';
import { X } from 'lucide-react';

export interface DashboardLayoutProps {
  header: ReactNode;
  sidebar?: ReactNode;
  children: ReactNode;
  footer?: ReactNode;
}

export const DashboardLayout = ({
  header,
  sidebar,
  children,
  footer
}: DashboardLayoutProps) => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const layoutStyles: CSSProperties = {
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    backgroundColor: 'var(--js-bg)',
    fontFamily: 'var(--js-font-system)'
  };

  const mainContainerStyles: CSSProperties = {
    display: 'flex',
    flex: 1,
    position: 'relative'
  };

  const sidebarStyles: CSSProperties = {
    width: 'var(--js-sidebar-width)',
    backgroundColor: 'var(--js-surface)',
    borderRight: `var(--js-border-width-thin) solid var(--js-border)`,
    overflowY: 'auto',
    position: 'sticky',
    top: 'var(--js-header-height)',
    height: 'calc(100vh - var(--js-header-height))',
    flexShrink: 0
  };

  const mobileSidebarOverlayStyles: CSSProperties = {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    zIndex: 999,
    display: sidebarOpen ? 'block' : 'none'
  };

  const mobileSidebarStyles: CSSProperties = {
    position: 'fixed',
    top: 0,
    left: sidebarOpen ? 0 : '-100%',
    bottom: 0,
    width: 'var(--js-sidebar-width)',
    maxWidth: '80vw',
    backgroundColor: 'var(--js-surface)',
    boxShadow: 'var(--js-shadow-4)',
    transition: 'left 300ms cubic-bezier(0.4, 0, 0.2, 1)',
    zIndex: 1000,
    overflowY: 'auto'
  };

  const contentStyles: CSSProperties = {
    flex: 1,
    padding: 'var(--js-space-xl) var(--js-space-lg)',
    maxWidth: 'var(--js-max-content-width)',
    margin: '0 auto',
    width: '100%'
  };

  const footerStyles: CSSProperties = {
    backgroundColor: 'var(--js-surface)',
    borderTop: `var(--js-border-width-thin) solid var(--js-border)`,
    padding: 'var(--js-space-lg)',
    marginTop: 'auto'
  };

  return (
    <div style={layoutStyles}>
      {header}

      <div style={mainContainerStyles}>
        {/* Desktop Sidebar */}
        {sidebar && (
          <aside style={sidebarStyles} className="desktop-only">
            {sidebar}
          </aside>
        )}

        {/* Mobile Sidebar */}
        {sidebar && (
          <>
            <div
              style={mobileSidebarOverlayStyles}
              onClick={() => setSidebarOpen(false)}
              className="mobile-only"
            />
            <aside style={mobileSidebarStyles} className="mobile-only">
              <div style={{
                display: 'flex',
                justifyContent: 'flex-end',
                padding: 'var(--js-space-md)'
              }}>
                <button
                  onClick={() => setSidebarOpen(false)}
                  style={{
                    background: 'none',
                    border: 'none',
                    cursor: 'pointer',
                    padding: 'var(--js-space-xs)',
                    color: 'var(--js-text)',
                    opacity: 0.6
                  }}
                >
                  <X size={24} />
                </button>
              </div>
              {sidebar}
            </aside>
          </>
        )}

        {/* Main Content */}
        <main style={contentStyles}>
          {children}
        </main>
      </div>

      {footer && <footer style={footerStyles}>{footer}</footer>}
    </div>
  );
};
