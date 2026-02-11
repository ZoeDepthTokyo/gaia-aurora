import { ReactNode, CSSProperties } from 'react';
import { ChevronUp, ChevronDown } from 'lucide-react';

export interface Column<T> {
  key: string;
  header: string;
  render?: (item: T) => ReactNode;
  sortable?: boolean;
  width?: string;
}

export interface DataTableProps<T> {
  data: T[];
  columns: Column<T>[];
  onRowClick?: (item: T) => void;
  sortBy?: string;
  sortDirection?: 'asc' | 'desc';
  onSort?: (key: string) => void;
  emptyState?: ReactNode;
  className?: string;
  style?: CSSProperties;
}

export function DataTable<T extends Record<string, any>>({
  data,
  columns,
  onRowClick,
  sortBy,
  sortDirection = 'asc',
  onSort,
  emptyState,
  className = '',
  style = {}
}: DataTableProps<T>) {
  const tableStyles: CSSProperties = {
    width: '100%',
    borderCollapse: 'collapse',
    fontFamily: 'var(--js-font-system)',
    ...style
  };

  const theadStyles: CSSProperties = {
    backgroundColor: 'var(--js-surface)',
    borderBottom: `var(--js-border-width-medium) solid var(--js-border)`
  };

  const thStyles: CSSProperties = {
    padding: 'var(--js-space-sm) var(--js-space-md)',
    textAlign: 'left',
    fontSize: 'var(--js-font-size-caption)',
    fontWeight: 'var(--js-font-weight-semibold)',
    letterSpacing: 'var(--js-letter-spacing-uppercase)',
    textTransform: 'uppercase',
    color: 'var(--js-text)',
    opacity: 0.7
  };

  const sortableThStyles: CSSProperties = {
    ...thStyles,
    cursor: 'pointer',
    userSelect: 'none'
  };

  const tdStyles: CSSProperties = {
    padding: 'var(--js-space-md)',
    fontSize: 'var(--js-font-size-body)',
    lineHeight: 'var(--js-line-height-body)',
    color: 'var(--js-text)',
    borderBottom: `var(--js-border-width-thin) solid var(--js-border)`
  };

  const rowStyles: CSSProperties = {
    cursor: onRowClick ? 'pointer' : 'default',
    transition: 'background-color 200ms'
  };

  if (data.length === 0 && emptyState) {
    return <div>{emptyState}</div>;
  }

  return (
    <div style={{ overflowX: 'auto' }} className={className}>
      <table style={tableStyles}>
        <thead style={theadStyles}>
          <tr>
            {columns.map((column) => (
              <th
                key={column.key}
                style={column.sortable ? sortableThStyles : thStyles}
                onClick={column.sortable && onSort ? () => onSort(column.key) : undefined}
                {...(column.width && { width: column.width })}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--js-space-xs)' }}>
                  {column.header}
                  {column.sortable && sortBy === column.key && (
                    sortDirection === 'asc' ? (
                      <ChevronUp size={14} />
                    ) : (
                      <ChevronDown size={14} />
                    )
                  )}
                </div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr
              key={index}
              style={rowStyles}
              onClick={onRowClick ? () => onRowClick(item) : undefined}
              onMouseEnter={(e) => {
                if (onRowClick) {
                  e.currentTarget.style.backgroundColor = 'var(--js-surface)';
                }
              }}
              onMouseLeave={(e) => {
                if (onRowClick) {
                  e.currentTarget.style.backgroundColor = 'transparent';
                }
              }}
            >
              {columns.map((column) => (
                <td key={column.key} style={tdStyles}>
                  {column.render ? column.render(item) : item[column.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
