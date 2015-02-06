%define extname ui
%define debug_package %{nil}

Name:           lv2-%{extname}
Version:        2.4
Release:        5
Summary:        LV2 %{extname} extension

Source:         http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
URL:            http://lv2plug.in/ns/extensions/%{extname}/
License:        ISC
Group:          System/Libraries
BuildRequires:  waf
BuildRequires:  pkgconfig
Requires:       lv2core

%description
This extension defines an interface that can be used in LV2 plugins and
hosts to create UIs for plugins. The UIs are similar to plugins and
reside in shared object files in an LV2 bundle.

%package    devel
Summary:    Development files for the LV2 %{extname} extension
Group:      Development/C
Requires:   %{name} = %{version}
Requires:   lv2core-devel

%description    devel
This package contains development files for the LV2 %{extname} extension.


%files
%defattr(-,root,root,-)
%{_libdir}/lv2/%{extname}.lv2/manifest.ttl
%{_libdir}/lv2/%{extname}.lv2/%{extname}.ttl
%{_libdir}/lv2/%{extname}.lv2/lv2-%{extname}.doap.ttl

%files devel
%{_includedir}/lv2/lv2plug.in/ns/extensions/%{extname}
%{_libdir}/lv2/%{extname}.lv2/%{extname}.h
%{_libdir}/pkgconfig/lv2-lv2plug.in-ns-extensions-%{extname}.pc

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
* Tue Apr 17 2012 Frank Kober <emuse@mandriva.org> 2.4-4
+ Revision: 791516
- fixed build arch which is not noarch

* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 2.4-3
+ Revision: 745045
- fix symlinking in devel package again

* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 2.4-2
+ Revision: 745036
- fix buildarch and devel package content

* Sat Nov 26 2011 Frank Kober <emuse@mandriva.org> 2.4-1
+ Revision: 733562
- new version 2.4
  o devel package added for new development files
  o file list adjusted
  o use of lv2config in %%post dropped (as of lv2core 6.0)

* Mon Jun 27 2011 Frank Kober <emuse@mandriva.org> 2.2-3
+ Revision: 687521
- despite no binaries this is not a noarch package

* Sun Jun 26 2011 Frank Kober <emuse@mandriva.org> 2.2-2
+ Revision: 687310
- bump release after last change
- fix BR, add lv2config to post

* Fri Jun 24 2011 Frank Kober <emuse@mandriva.org> 2.2-1
+ Revision: 686942
- imported package lv2-ui

