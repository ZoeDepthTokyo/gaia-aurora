import React, { useState, useEffect } from 'react';
import { Card } from './molecules/Card';
import { Button } from './atoms/Button';

// Import current tokens
import colorsData from '../tokens/colors.json';
import typographyData from '../tokens/typography.json';
import spacingData from '../tokens/spacing.json';
import shadowsData from '../tokens/shadows.json';
import bordersData from '../tokens/borders.json';

interface ColorValue {
  default: string;
  hover?: string;
  active?: string;
}

interface DesignTokens {
  colors: typeof colorsData;
  typography: typeof typographyData;
  spacing: typeof spacingData;
  shadows: typeof shadowsData;
  borders: typeof bordersData;
}

export const DesignTokenEditor: React.FC = () => {
  const [tokens, setTokens] = useState<DesignTokens>({
    colors: colorsData,
    typography: typographyData,
    spacing: spacingData,
    shadows: shadowsData,
    borders: bordersData,
  });

  const [activeTab, setActiveTab] = useState<'colors' | 'typography' | 'spacing' | 'shadows' | 'borders'>('colors');
  const [mode, setMode] = useState<'light' | 'dark'>('light');

  // Apply tokens to CSS variables in real-time
  useEffect(() => {
    const root = document.documentElement;

    // Apply colors
    const modeColors = tokens.colors.color.mode[mode];
    root.style.setProperty('--js-primary', modeColors.primary.default);
    root.style.setProperty('--js-primary-hover', modeColors.primary.hover || modeColors.primary.default);
    root.style.setProperty('--js-secondary', modeColors.secondary.default);
    root.style.setProperty('--js-success', modeColors.semantic.success);
    root.style.setProperty('--js-error', modeColors.semantic.error);
    root.style.setProperty('--js-warning', modeColors.semantic.warning);
    root.style.setProperty('--js-bg', modeColors.neutral.bg);
    root.style.setProperty('--js-surface', modeColors.neutral.surface);
    root.style.setProperty('--js-border', modeColors.neutral.border);
    root.style.setProperty('--js-text', modeColors.neutral.text);

    // Apply typography
    root.style.setProperty('--js-font-size-h1', tokens.typography.typography.fontSize.h1);
    root.style.setProperty('--js-font-size-h2', tokens.typography.typography.fontSize.h2);
    root.style.setProperty('--js-font-size-h3', tokens.typography.typography.fontSize.h3);
    root.style.setProperty('--js-font-size-body', tokens.typography.typography.fontSize.body);

    // Apply spacing
    root.style.setProperty('--js-space-xs', tokens.spacing.spacing.scale.xs);
    root.style.setProperty('--js-space-sm', tokens.spacing.spacing.scale.sm);
    root.style.setProperty('--js-space-md', tokens.spacing.spacing.scale.md);
    root.style.setProperty('--js-space-lg', tokens.spacing.spacing.scale.lg);
    root.style.setProperty('--js-space-xl', tokens.spacing.spacing.scale.xl);
  }, [tokens, mode]);

  const updateColor = (path: string, value: string) => {
    const newTokens = JSON.parse(JSON.stringify(tokens));
    const keys = path.split('.');
    let obj: any = newTokens.colors.color.mode[mode];
    for (let i = 0; i < keys.length - 1; i++) {
      obj = obj[keys[i]];
    }
    obj[keys[keys.length - 1]] = value;
    setTokens(newTokens);
  };

  const updateTypography = (category: string, property: string, value: string) => {
    const newTokens = JSON.parse(JSON.stringify(tokens));
    newTokens.typography.typography[category][property] = value;
    setTokens(newTokens);
  };

  const updateSpacing = (key: string, value: string) => {
    const newTokens = JSON.parse(JSON.stringify(tokens));
    newTokens.spacing.spacing.scale[key] = value;
    setTokens(newTokens);
  };

  const hexToRgb = (hex: string) => {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : null;
  };

  const rgbToHex = (r: number, g: number, b: number) => {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
  };

  const downloadTokens = () => {
    const dataStr = JSON.stringify(tokens, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
    const exportFileDefaultName = 'jseeker-design-tokens.json';
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
  };

  const resetToDefaults = () => {
    setTokens({
      colors: colorsData,
      typography: typographyData,
      spacing: spacingData,
      shadows: shadowsData,
      borders: bordersData,
    });
  };

  const modeColors = tokens.colors.color.mode[mode];

  return (
    <div style={{
      minHeight: '100vh',
      background: 'var(--js-bg)',
      color: 'var(--js-text)',
      fontFamily: 'var(--js-font-system)'
    }}>
      {/* Header */}
      <div style={{
        borderBottom: '1px solid var(--js-border)',
        padding: '16px 24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        background: 'var(--js-surface)'
      }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '24px', fontWeight: 700 }}>jSeeker Design Token Editor</h1>
          <p style={{ margin: '4px 0 0', fontSize: '14px', opacity: 0.7 }}>
            Adjust design tokens in real-time. Changes apply to preview components instantly.
          </p>
        </div>
        <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
          <select
            value={mode}
            onChange={(e) => setMode(e.target.value as 'light' | 'dark')}
            style={{
              padding: '8px 12px',
              borderRadius: '4px',
              border: '1px solid var(--js-border)',
              background: 'var(--js-bg)',
              color: 'var(--js-text)',
              fontSize: '14px'
            }}
          >
            <option value="light">Light Mode</option>
            <option value="dark">Dark Mode</option>
          </select>
          <Button onClick={resetToDefaults} variant="secondary">Reset</Button>
          <Button onClick={downloadTokens}>Export JSON</Button>
        </div>
      </div>

      <div style={{ display: 'flex', height: 'calc(100vh - 89px)' }}>
        {/* Sidebar - Token Controls */}
        <div style={{
          width: '400px',
          borderRight: '1px solid var(--js-border)',
          overflowY: 'auto',
          background: 'var(--js-surface)',
          padding: '16px'
        }}>
          {/* Tabs */}
          <div style={{ display: 'flex', gap: '8px', marginBottom: '16px', flexWrap: 'wrap' }}>
            {(['colors', 'typography', 'spacing', 'shadows', 'borders'] as const).map(tab => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                style={{
                  padding: '8px 16px',
                  borderRadius: '4px',
                  border: activeTab === tab ? '2px solid var(--js-primary)' : '1px solid var(--js-border)',
                  background: activeTab === tab ? 'var(--js-primary)' : 'var(--js-bg)',
                  color: activeTab === tab ? 'white' : 'var(--js-text)',
                  fontSize: '14px',
                  fontWeight: 600,
                  cursor: 'pointer',
                  textTransform: 'capitalize'
                }}
              >
                {tab}
              </button>
            ))}
          </div>

          {/* Colors Panel */}
          {activeTab === 'colors' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
              <ColorSection
                title="Primary"
                color={modeColors.primary.default}
                onChange={(val) => updateColor('primary.default', val)}
              />
              <ColorSection
                title="Primary Hover"
                color={modeColors.primary.hover || modeColors.primary.default}
                onChange={(val) => updateColor('primary.hover', val)}
              />
              <ColorSection
                title="Secondary"
                color={modeColors.secondary.default}
                onChange={(val) => updateColor('secondary.default', val)}
              />
              <ColorSection
                title="Success"
                color={modeColors.semantic.success}
                onChange={(val) => updateColor('semantic.success', val)}
              />
              <ColorSection
                title="Warning"
                color={modeColors.semantic.warning}
                onChange={(val) => updateColor('semantic.warning', val)}
              />
              <ColorSection
                title="Error"
                color={modeColors.semantic.error}
                onChange={(val) => updateColor('semantic.error', val)}
              />
              <ColorSection
                title="Background"
                color={modeColors.neutral.bg}
                onChange={(val) => updateColor('neutral.bg', val)}
              />
              <ColorSection
                title="Surface"
                color={modeColors.neutral.surface}
                onChange={(val) => updateColor('neutral.surface', val)}
              />
              <ColorSection
                title="Border"
                color={modeColors.neutral.border}
                onChange={(val) => updateColor('neutral.border', val)}
              />
              <ColorSection
                title="Text"
                color={modeColors.neutral.text}
                onChange={(val) => updateColor('neutral.text', val)}
              />
            </div>
          )}

          {/* Typography Panel */}
          {activeTab === 'typography' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
              <SliderControl
                label="H1 Size"
                value={parseInt(tokens.typography.typography.fontSize.h1)}
                min={24}
                max={72}
                unit="px"
                onChange={(val) => updateTypography('fontSize', 'h1', `${val}px`)}
              />
              <SliderControl
                label="H2 Size"
                value={parseInt(tokens.typography.typography.fontSize.h2)}
                min={18}
                max={48}
                unit="px"
                onChange={(val) => updateTypography('fontSize', 'h2', `${val}px`)}
              />
              <SliderControl
                label="H3 Size"
                value={parseInt(tokens.typography.typography.fontSize.h3)}
                min={14}
                max={32}
                unit="px"
                onChange={(val) => updateTypography('fontSize', 'h3', `${val}px`)}
              />
              <SliderControl
                label="Body Size"
                value={parseInt(tokens.typography.typography.fontSize.body)}
                min={12}
                max={20}
                unit="px"
                onChange={(val) => updateTypography('fontSize', 'body', `${val}px`)}
              />
              <SliderControl
                label="Caption Size"
                value={parseInt(tokens.typography.typography.fontSize.caption)}
                min={10}
                max={16}
                unit="px"
                onChange={(val) => updateTypography('fontSize', 'caption', `${val}px`)}
              />
            </div>
          )}

          {/* Spacing Panel */}
          {activeTab === 'spacing' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
              <SliderControl
                label="XS Spacing"
                value={parseInt(tokens.spacing.spacing.scale.xs)}
                min={2}
                max={8}
                unit="px"
                onChange={(val) => updateSpacing('xs', `${val}px`)}
              />
              <SliderControl
                label="SM Spacing"
                value={parseInt(tokens.spacing.spacing.scale.sm)}
                min={4}
                max={16}
                unit="px"
                onChange={(val) => updateSpacing('sm', `${val}px`)}
              />
              <SliderControl
                label="MD Spacing"
                value={parseInt(tokens.spacing.spacing.scale.md)}
                min={8}
                max={24}
                unit="px"
                onChange={(val) => updateSpacing('md', `${val}px`)}
              />
              <SliderControl
                label="LG Spacing"
                value={parseInt(tokens.spacing.spacing.scale.lg)}
                min={16}
                max={40}
                unit="px"
                onChange={(val) => updateSpacing('lg', `${val}px`)}
              />
              <SliderControl
                label="XL Spacing"
                value={parseInt(tokens.spacing.spacing.scale.xl)}
                min={24}
                max={64}
                unit="px"
                onChange={(val) => updateSpacing('xl', `${val}px`)}
              />
              <SliderControl
                label="XXL Spacing"
                value={parseInt(tokens.spacing.spacing.scale.xxl)}
                min={32}
                max={96}
                unit="px"
                onChange={(val) => updateSpacing('xxl', `${val}px`)}
              />
            </div>
          )}
        </div>

        {/* Preview Panel */}
        <div style={{
          flex: 1,
          overflowY: 'auto',
          padding: '24px',
          background: 'var(--js-bg)'
        }}>
          <ComponentPreview />
        </div>
      </div>
    </div>
  );
};

// Color Section Component
const ColorSection: React.FC<{ title: string; color: string; onChange: (color: string) => void }> = ({ title, color, onChange }) => {
  const hexToRgb = (hex: string) => {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
      r: parseInt(result[1], 16),
      g: parseInt(result[2], 16),
      b: parseInt(result[3], 16)
    } : { r: 0, g: 0, b: 0 };
  };

  const rgbToHex = (r: number, g: number, b: number) => {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
  };

  const rgb = hexToRgb(color);
  const [r, setR] = React.useState(rgb.r);
  const [g, setG] = React.useState(rgb.g);
  const [b, setB] = React.useState(rgb.b);

  React.useEffect(() => {
    const newRgb = hexToRgb(color);
    setR(newRgb.r);
    setG(newRgb.g);
    setB(newRgb.b);
  }, [color]);

  const handleColorChange = (channel: 'r' | 'g' | 'b', value: number) => {
    const newR = channel === 'r' ? value : r;
    const newG = channel === 'g' ? value : g;
    const newB = channel === 'b' ? value : b;
    setR(newR);
    setG(newG);
    setB(newB);
    onChange(rgbToHex(newR, newG, newB));
  };

  return (
    <div style={{
      padding: '16px',
      borderRadius: '8px',
      background: 'var(--js-bg)',
      border: '1px solid var(--js-border)'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
        <label style={{ fontSize: '14px', fontWeight: 600 }}>{title}</label>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <input
            type="color"
            value={color}
            onChange={(e) => onChange(e.target.value)}
            style={{ width: '40px', height: '40px', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
          />
          <input
            type="text"
            value={color.toUpperCase()}
            onChange={(e) => {
              if (/^#[0-9A-F]{6}$/i.test(e.target.value)) {
                onChange(e.target.value);
              }
            }}
            style={{
              width: '80px',
              padding: '8px',
              fontSize: '12px',
              fontFamily: 'monospace',
              border: '1px solid var(--js-border)',
              borderRadius: '4px',
              background: 'var(--js-surface)',
              color: 'var(--js-text)'
            }}
          />
        </div>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        <SliderRow label="R" value={r} onChange={(val) => handleColorChange('r', val)} color="#ff0000" />
        <SliderRow label="G" value={g} onChange={(val) => handleColorChange('g', val)} color="#00ff00" />
        <SliderRow label="B" value={b} onChange={(val) => handleColorChange('b', val)} color="#0000ff" />
      </div>
    </div>
  );
};

// Slider Row Component
const SliderRow: React.FC<{ label: string; value: number; onChange: (val: number) => void; color?: string }> = ({ label, value, onChange, color }) => (
  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
    <span style={{ fontSize: '12px', fontWeight: 600, width: '20px', opacity: 0.7 }}>{label}</span>
    <input
      type="range"
      min="0"
      max="255"
      value={value}
      onChange={(e) => onChange(parseInt(e.target.value))}
      style={{
        flex: 1,
        accentColor: color || 'var(--js-primary)'
      }}
    />
    <span style={{
      fontSize: '12px',
      fontFamily: 'monospace',
      width: '35px',
      textAlign: 'right',
      opacity: 0.7
    }}>{value}</span>
  </div>
);

// Slider Control Component
const SliderControl: React.FC<{
  label: string;
  value: number;
  min: number;
  max: number;
  unit?: string;
  onChange: (val: number) => void;
}> = ({ label, value, min, max, unit = '', onChange }) => (
  <div style={{
    padding: '16px',
    borderRadius: '8px',
    background: 'var(--js-bg)',
    border: '1px solid var(--js-border)'
  }}>
    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '12px' }}>
      <label style={{ fontSize: '14px', fontWeight: 600 }}>{label}</label>
      <span style={{
        fontSize: '14px',
        fontFamily: 'monospace',
        fontWeight: 600,
        color: 'var(--js-primary)'
      }}>
        {value}{unit}
      </span>
    </div>
    <input
      type="range"
      min={min}
      max={max}
      value={value}
      onChange={(e) => onChange(parseInt(e.target.value))}
      style={{
        width: '100%',
        accentColor: 'var(--js-primary)'
      }}
    />
  </div>
);

// Component Preview
const ComponentPreview: React.FC = () => (
  <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
    <h2 style={{ fontSize: 'var(--js-font-size-h2)', marginBottom: '24px' }}>Live Component Preview</h2>

    <div style={{ display: 'flex', flexDirection: 'column', gap: '32px' }}>
      {/* Typography Preview */}
      <section>
        <h3 style={{ fontSize: 'var(--js-font-size-h3)', marginBottom: '16px' }}>Typography</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '24px', background: 'var(--js-surface)', borderRadius: '8px' }}>
          <h1 style={{ fontSize: 'var(--js-font-size-h1)', margin: 0 }}>Heading 1</h1>
          <h2 style={{ fontSize: 'var(--js-font-size-h2)', margin: 0 }}>Heading 2</h2>
          <h3 style={{ fontSize: 'var(--js-font-size-h3)', margin: 0 }}>Heading 3</h3>
          <p style={{ fontSize: 'var(--js-font-size-body)', margin: 0 }}>Body text - The quick brown fox jumps over the lazy dog.</p>
          <p style={{ fontSize: 'var(--js-font-size-caption)', margin: 0, opacity: 0.7 }}>Caption text - Supporting information</p>
        </div>
      </section>

      {/* Colors Preview */}
      <section>
        <h3 style={{ fontSize: 'var(--js-font-size-h3)', marginBottom: '16px' }}>Colors</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(150px, 1fr))', gap: '16px' }}>
          {[
            { name: 'Primary', color: 'var(--js-primary)' },
            { name: 'Secondary', color: 'var(--js-secondary)' },
            { name: 'Success', color: 'var(--js-success)' },
            { name: 'Warning', color: 'var(--js-warning)' },
            { name: 'Error', color: 'var(--js-error)' },
            { name: 'Surface', color: 'var(--js-surface)' },
          ].map(({ name, color }) => (
            <div key={name} style={{ textAlign: 'center' }}>
              <div style={{
                height: '80px',
                background: color,
                borderRadius: '8px',
                border: '1px solid var(--js-border)',
                marginBottom: '8px'
              }} />
              <span style={{ fontSize: '12px', opacity: 0.7 }}>{name}</span>
            </div>
          ))}
        </div>
      </section>

      {/* Buttons Preview */}
      <section>
        <h3 style={{ fontSize: 'var(--js-font-size-h3)', marginBottom: '16px' }}>Buttons</h3>
        <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', padding: '24px', background: 'var(--js-surface)', borderRadius: '8px' }}>
          <button style={{
            padding: 'var(--js-space-sm) var(--js-space-md)',
            background: 'var(--js-primary)',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            fontSize: 'var(--js-font-size-body)',
            fontWeight: 600,
            cursor: 'pointer'
          }}>Primary</button>
          <button style={{
            padding: 'var(--js-space-sm) var(--js-space-md)',
            background: 'var(--js-secondary)',
            color: 'var(--js-text)',
            border: 'none',
            borderRadius: '4px',
            fontSize: 'var(--js-font-size-body)',
            fontWeight: 600,
            cursor: 'pointer'
          }}>Secondary</button>
          <button style={{
            padding: 'var(--js-space-sm) var(--js-space-md)',
            background: 'var(--js-success)',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            fontSize: 'var(--js-font-size-body)',
            fontWeight: 600,
            cursor: 'pointer'
          }}>Success</button>
          <button style={{
            padding: 'var(--js-space-sm) var(--js-space-md)',
            background: 'var(--js-error)',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            fontSize: 'var(--js-font-size-body)',
            fontWeight: 600,
            cursor: 'pointer'
          }}>Error</button>
        </div>
      </section>

      {/* Spacing Preview */}
      <section>
        <h3 style={{ fontSize: 'var(--js-font-size-h3)', marginBottom: '16px' }}>Spacing Scale</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', padding: '24px', background: 'var(--js-surface)', borderRadius: '8px' }}>
          {['xs', 'sm', 'md', 'lg', 'xl', 'xxl'].map(size => (
            <div key={size} style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
              <span style={{ fontSize: '12px', width: '40px', opacity: 0.7, fontWeight: 600 }}>{size.toUpperCase()}</span>
              <div style={{
                height: '24px',
                width: `var(--js-space-${size})`,
                background: 'var(--js-primary)',
                borderRadius: '4px'
              }} />
              <span style={{ fontSize: '12px', opacity: 0.5, fontFamily: 'monospace' }}>
                var(--js-space-{size})
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* Card Preview */}
      <section>
        <h3 style={{ fontSize: 'var(--js-font-size-h3)', marginBottom: '16px' }}>Cards</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '16px' }}>
          <div style={{
            padding: 'var(--js-space-lg)',
            background: 'var(--js-surface)',
            borderRadius: '8px',
            border: '1px solid var(--js-border)'
          }}>
            <h4 style={{ fontSize: 'var(--js-font-size-h3)', margin: '0 0 8px' }}>Card Title</h4>
            <p style={{ fontSize: 'var(--js-font-size-body)', margin: '0', opacity: 0.7 }}>
              Card content with spacing applied from design tokens.
            </p>
          </div>
          <div style={{
            padding: 'var(--js-space-lg)',
            background: 'var(--js-surface)',
            borderRadius: '8px',
            border: '1px solid var(--js-border)'
          }}>
            <h4 style={{ fontSize: 'var(--js-font-size-h3)', margin: '0 0 8px' }}>Another Card</h4>
            <p style={{ fontSize: 'var(--js-font-size-body)', margin: '0', opacity: 0.7 }}>
              Real-time updates as you adjust the sliders.
            </p>
          </div>
        </div>
      </section>
    </div>
  </div>
);

export default DesignTokenEditor;
