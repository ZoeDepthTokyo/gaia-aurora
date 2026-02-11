import { CSSProperties, useState } from 'react';
import { Search, SlidersHorizontal, X } from 'lucide-react';
import { Input } from '../atoms/Input';
import { Button } from '../atoms/Button';
import { Select } from '../atoms/Select';
import { Badge } from '../molecules/Badge';

export interface FilterOption {
  key: string;
  label: string;
  type: 'select' | 'multiselect';
  options: { value: string; label: string }[];
}

export interface SearchFilterBarProps {
  searchPlaceholder?: string;
  onSearch?: (query: string) => void;
  filters?: FilterOption[];
  activeFilters?: Record<string, string | string[]>;
  onFilterChange?: (key: string, value: string | string[]) => void;
  onClearFilters?: () => void;
}

export const SearchFilterBar = ({
  searchPlaceholder = 'Search...',
  onSearch,
  filters = [],
  activeFilters = {},
  onFilterChange,
  onClearFilters
}: SearchFilterBarProps) => {
  const [showFilters, setShowFilters] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  const containerStyles: CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: 'var(--js-space-md)',
    fontFamily: 'var(--js-font-system)'
  };

  const searchRowStyles: CSSProperties = {
    display: 'flex',
    gap: 'var(--js-space-sm)',
    alignItems: 'center'
  };

  const filtersPanelStyles: CSSProperties = {
    display: showFilters ? 'flex' : 'none',
    flexDirection: 'column',
    gap: 'var(--js-space-md)',
    padding: 'var(--js-space-md)',
    backgroundColor: 'var(--js-surface)',
    border: `var(--js-border-width-thin) solid var(--js-border)`,
    borderRadius: 'var(--js-border-radius-md)'
  };

  const filtersGridStyles: CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
    gap: 'var(--js-space-md)'
  };

  const activeFiltersStyles: CSSProperties = {
    display: 'flex',
    flexWrap: 'wrap',
    gap: 'var(--js-space-xs)',
    alignItems: 'center'
  };

  const activeFilterCount = Object.keys(activeFilters).filter(
    key => activeFilters[key] && (Array.isArray(activeFilters[key]) ? activeFilters[key].length > 0 : activeFilters[key])
  ).length;

  return (
    <div style={containerStyles}>
      <div style={searchRowStyles}>
        <div style={{ flex: 1 }}>
          <Input
            placeholder={searchPlaceholder}
            prefixIcon={<Search size={20} />}
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              onSearch?.(e.target.value);
            }}
            fullWidth
          />
        </div>
        {filters.length > 0 && (
          <Button
            variant={showFilters ? 'primary' : 'secondary'}
            iconLeft={<SlidersHorizontal size={20} />}
            onClick={() => setShowFilters(!showFilters)}
          >
            Filters
            {activeFilterCount > 0 && ` (${activeFilterCount})`}
          </Button>
        )}
      </div>

      {activeFilterCount > 0 && (
        <div style={activeFiltersStyles}>
          <span style={{
            fontSize: 'var(--js-font-size-caption)',
            color: 'var(--js-text)',
            opacity: 0.6
          }}>
            Active filters:
          </span>
          {Object.entries(activeFilters).map(([key, value]) => {
            if (!value || (Array.isArray(value) && value.length === 0)) return null;
            const filter = filters.find(f => f.key === key);
            const displayValue = Array.isArray(value) ? value.join(', ') : value;
            return (
              <Badge key={key} variant="default">
                {filter?.label}: {displayValue}
                <button
                  onClick={() => onFilterChange?.(key, Array.isArray(value) ? [] : '')}
                  style={{
                    background: 'none',
                    border: 'none',
                    padding: 0,
                    marginLeft: 'var(--js-space-xs)',
                    cursor: 'pointer',
                    display: 'inline-flex',
                    color: 'inherit'
                  }}
                >
                  <X size={12} />
                </button>
              </Badge>
            );
          })}
          <Button
            variant="ghost"
            size="sm"
            onClick={onClearFilters}
          >
            Clear all
          </Button>
        </div>
      )}

      {showFilters && (
        <div style={filtersPanelStyles}>
          <div style={filtersGridStyles}>
            {filters.map((filter) => (
              <div key={filter.key}>
                <label style={{
                  fontSize: 'var(--js-font-size-caption)',
                  fontWeight: 'var(--js-font-weight-semibold)',
                  color: 'var(--js-text)',
                  display: 'block',
                  marginBottom: 'var(--js-space-xs)',
                  textTransform: 'uppercase',
                  letterSpacing: 'var(--js-letter-spacing-uppercase)'
                }}>
                  {filter.label}
                </label>
                <Select
                  value={(activeFilters[filter.key] as string) || ''}
                  onChange={(e) => onFilterChange?.(filter.key, e.target.value)}
                  fullWidth
                >
                  <option value="">All</option>
                  {filter.options.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </Select>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
