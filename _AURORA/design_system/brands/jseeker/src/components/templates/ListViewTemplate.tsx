import { ReactNode, CSSProperties } from 'react';
import { SearchFilterBar, SearchFilterBarProps } from '../organisms/SearchFilterBar';
import { EmptyState } from '../molecules/EmptyState';

export interface ListViewTemplateProps {
  title: string;
  subtitle?: string;
  actions?: ReactNode;
  searchFilter?: SearchFilterBarProps;
  children: ReactNode;
  isEmpty?: boolean;
  emptyState?: ReactNode;
  pagination?: ReactNode;
}

export const ListViewTemplate = ({
  title,
  subtitle,
  actions,
  searchFilter,
  children,
  isEmpty = false,
  emptyState,
  pagination
}: ListViewTemplateProps) => {
  const containerStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-xl)',
    fontFamily: 'var(--js-font-system)'
  };

  const headerStyles: CSSProperties = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    gap: 'var(--js-space-md)',
    paddingBottom: 'var(--js-space-md)',
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
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    opacity: 0.7,
    margin: 0
  };

  const contentStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-lg)'
  };

  return (
    <div style={containerStyles}>
      {/* Header */}
      <div style={headerStyles}>
        <div style={headerContentStyles}>
          <h1 style={titleStyles}>{title}</h1>
          {subtitle && <p style={subtitleStyles}>{subtitle}</p>}
        </div>
        {actions && <div>{actions}</div>}
      </div>

      {/* Search & Filters */}
      {searchFilter && <SearchFilterBar {...searchFilter} />}

      {/* Content or Empty State */}
      {isEmpty ? (
        emptyState || <EmptyState title="No results found" description="Try adjusting your search or filters" />
      ) : (
        <div style={contentStyles}>{children}</div>
      )}

      {/* Pagination */}
      {pagination && !isEmpty && (
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          paddingTop: 'var(--js-space-lg)',
          borderTop: `var(--js-border-width-thin) solid var(--js-border)`
        }}>
          {pagination}
        </div>
      )}
    </div>
  );
};
