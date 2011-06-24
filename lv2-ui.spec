Name:           lv2-ui
Version:        2.2
Release:        %mkrel 1
Summary:        LV2 UI extension

Source:         http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
URL:            http://lv2plug.in/ns/extensions/ui/
License:        ISC
Group:          System/Libraries
BuildArch:      noarch
BuildRequires:  waf
Requires:       slv2-devel

%description
This extension defines an interface that can be used in LV2 plugins and
hosts to create UIs for plugins. The UIs are similar to plugins and
reside in shared object files in an LV2 bundle.

%files
%defattr(-,root,root,-)
%{_libdir}/lv2/ui.lv2/manifest.ttl
%{_libdir}/lv2/ui.lv2/ui.h
%{_libdir}/lv2/ui.lv2/ui.ttl
%{_libdir}/lv2/ui.lv2/.lock-wafbuild

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


