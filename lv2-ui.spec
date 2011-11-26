Name:           lv2-ui
Version:        2.4
Release:        1
Summary:        LV2 UI extension

Source:         http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
URL:            http://lv2plug.in/ns/extensions/ui/
License:        ISC
Group:          System/Libraries
BuildRequires:  waf
BuildRequires:  pkgconfig
Requires:       lv2core-devel >= 0.4

%description
This extension defines an interface that can be used in LV2 plugins and
hosts to create UIs for plugins. The UIs are similar to plugins and
reside in shared object files in an LV2 bundle.

%package    devel
Summary:    Development files for the LV2 UI extension
Group:      Development/C
Requires:   %{name} = %{version}

%description    devel
This package contains development files for the LV2 UI extension.


%files
%defattr(-,root,root,-)
%{_libdir}/lv2/ui.lv2/manifest.ttl
%{_libdir}/lv2/ui.lv2/ui.h
%{_libdir}/lv2/ui.lv2/ui.ttl
%{_libdir}/lv2/ui.lv2/lv2-ui.doap.ttl

%files devel
%{_includedir}/lv2/lv2plug.in/ns/extensions/ui
%{_libdir}/pkgconfig/lv2-lv2plug.in-ns-extensions-ui.pc

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
./waf

%install
rm -rf %{buildroot}

./waf install --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%changelog
